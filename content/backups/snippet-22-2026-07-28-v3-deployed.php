/**
 * Volado Labs — Elementor CSS integrity guard (permanent). v3 — 2026-07-28.
 * Fixes recurring "unstyled / flush-left / blank-hero" renders caused by
 * Elementor persisting INCOMPLETE per-page CSS that page caches then freeze.
 *
 * v1: caught TOTAL poisoning only (containers but zero `--display` rules).
 * v2: added PARTIAL detection for classic background images (the 2026-07-28
 *     blank-hero incident: hero band fe996ad lost its background block while
 *     all `--display` rules were intact, so v1 saw `--display` and skipped it).
 * v3 (per Henry's review): (a) also verify a declared non-zero `min_height`
 *     renders (value-specific, low false-positive risk); (b) RATE-LIMIT the
 *     front-end self-heal with a per-post cooldown transient so a genuinely
 *     un-healable page can never spin into a regen loop on every request;
 *     (c) LOG the specific element:declaration that was missing when a repair
 *     fires. The checked set is deliberately kept TIGHT (classic backgrounds +
 *     value-specific min-height) — declarations Elementor reliably emits — to
 *     avoid false positives, since false positives are exactly what the
 *     cooldown has to defend against. Widths/responsive are intentionally NOT
 *     asserted (Elementor legitimately omits defaulted/inherited values).
 */

/* ---- integrity helpers ---------------------------------------------------- */

// Requirements this page's data implies: [{eid, needle, label}, ...].
if (!function_exists('volado_css_requirements')) {
    function volado_css_requirements($data) {
        $req = array();
        if (!is_string($data) || $data === '') { return $req; }
        $tree = json_decode($data, true);
        if (!is_array($tree)) { return $req; } // undecodable -> only total check runs
        $walk = function ($els) use (&$walk, &$req) {
            foreach ((array) $els as $el) {
                if (!is_array($el)) { continue; }
                $id = !empty($el['id']) ? $el['id'] : '';
                $s  = (isset($el['settings']) && is_array($el['settings'])) ? $el['settings'] : array();
                if ($id) {
                    // classic (rendered) background image
                    if (
                        isset($s['background_background']) && $s['background_background'] === 'classic' &&
                        !empty($s['background_image']['url']) &&
                        strpos($s['background_image']['url'], 'http') === 0
                    ) {
                        $req[] = array('eid' => $id, 'needle' => 'background-image:url', 'label' => $id . ':background-image');
                    }
                    // non-zero min-height (value-specific to dodge the 0px reset rule)
                    if (isset($s['min_height']['size']) && is_numeric($s['min_height']['size']) && $s['min_height']['size'] > 0) {
                        $unit = !empty($s['min_height']['unit']) ? $s['min_height']['unit'] : 'px';
                        $sz   = $s['min_height']['size'] + 0;
                        $val  = (floor($sz) == $sz) ? (string) intval($sz) : (string) $sz;
                        $req[] = array('eid' => $id, 'needle' => 'min-height:' . $val . $unit, 'label' => $id . ':min-height:' . $val . $unit);
                    }
                }
                if (!empty($el['elements'])) { $walk($el['elements']); }
            }
        };
        $walk($tree);
        return $req;
    }
}

// Does any CSS rule-block whose selector contains this element have $needle?
if (!function_exists('volado_css_el_has_decl')) {
    function volado_css_el_has_decl($css, $eid, $needle) {
        $sel = 'elementor-element-' . $eid;
        $sp = strpos($css, $sel);
        while ($sp !== false) {
            $brace = strpos($css, '{', $sp);
            if ($brace === false) { break; }
            $end = strpos($css, '}', $brace);
            if ($end === false) { $end = strlen($css); }
            if (strpos(substr($css, $brace, $end - $brace), $needle) !== false) { return true; }
            $sp = strpos($css, $sel, $brace);
        }
        return false;
    }
}

// '' if the generated CSS looks complete; else a short list of what's missing.
if (!function_exists('volado_css_missing')) {
    function volado_css_missing($data, $css) {
        if (!is_string($css) || $css === '') { return 'empty-css'; }
        if (strpos($data, '"elType":"container"') !== false && strpos($css, '--display') === false) {
            return 'no--display';
        }
        $miss = array();
        foreach (volado_css_requirements($data) as $r) {
            if (!volado_css_el_has_decl($css, $r['eid'], $r['needle'])) { $miss[] = $r['label']; }
        }
        return implode(',', array_slice($miss, 0, 5));
    }
}

// Regenerate CSS and verify; one retry if still incomplete. Stamps a
// per-generation "verified good" signature so the front-end check can skip.
// Returns '' on success, or the still-missing descriptor on failure.
if (!function_exists('volado_css_regen_verify')) {
    function volado_css_regen_verify($id) {
        if (!class_exists('\Elementor\Plugin')) { return 'no-elementor'; }
        $data = get_post_meta($id, '_elementor_data', true);
        $last = 'regen-failed';
        for ($i = 0; $i < 2; $i++) {
            try { \Elementor\Core\Files\CSS\Post::create((int) $id)->update(); }
            catch (\Throwable $e) { return 'exception'; }
            $meta = get_post_meta($id, '_elementor_css', true);
            $css  = (is_array($meta) && isset($meta['css']) && is_string($meta['css'])) ? $meta['css'] : '';
            $last = volado_css_missing($data, $css);
            if ($last === '') {
                update_post_meta($id, '_volado_css_ok_sig', md5($css));
                return '';
            }
        }
        return $last;
    }
}

/* ---- A) after ANY Elementor cache purge: regen every post, verified ------- */
add_action('elementor/core/files/clear_cache', function () {
    if (!class_exists('\Elementor\Plugin')) { return; }
    ignore_user_abort(true);
    if (function_exists('set_time_limit')) { @set_time_limit(600); }
    global $wpdb;
    $ids = $wpdb->get_col("SELECT DISTINCT pm.post_id FROM {$wpdb->postmeta} pm JOIN {$wpdb->posts} p ON p.ID = pm.post_id WHERE pm.meta_key = '_elementor_data' AND pm.meta_value LIKE '[%' AND p.post_status IN ('publish','private','draft')");
    $ok = 0; $bad = array();
    foreach ($ids as $id) {
        $m = volado_css_regen_verify((int) $id);
        if ($m === '') { $ok++; } else { $bad[] = $id . '(' . $m . ')'; }
    }
    update_option('volado_css_regen_log', $ok . ' ok / ' . count($bad) . ' incomplete of ' . count($ids) . ' @' . gmdate('c') . (empty($bad) ? '' : ' :: ' . implode(' ', array_slice($bad, 0, 10))), false);
    try { do_action('siteground_optimizer_flush_cache'); } catch (\Throwable $e) {}
}, 999);

/* ---- B) front-end self-heal: total/partial, rate-limited, logged ---------- */
add_action('wp', function () {
    if (is_admin() || !is_singular()) { return; }
    $id = get_the_ID();
    if (!$id || !class_exists('\Elementor\Plugin')) { return; }
    $data = get_post_meta($id, '_elementor_data', true);
    if (!is_string($data) || strpos($data, '"elType":"container"') === false) { return; }
    $meta = get_post_meta($id, '_elementor_css', true);
    if (!is_array($meta) || empty($meta['status']) || !isset($meta['css']) || !is_string($meta['css'])) { return; }
    $css = $meta['css'];
    $sig = md5($css);
    if (get_post_meta($id, '_volado_css_ok_sig', true) === $sig) { return; } // verified good this build
    $missing = volado_css_missing($data, $css);
    if ($missing === '') {                                                     // healthy -> stamp + skip
        update_post_meta($id, '_volado_css_ok_sig', $sig);
        return;
    }
    // poisoned. RATE LIMIT: at most one heal attempt per post per cooldown,
    // so a page that cannot be healed can never loop on every request.
    $ckey = 'volado_css_heal_' . $id;
    if (get_transient($ckey)) { return; }
    set_transient($ckey, gmdate('c') . '|' . $missing, 10 * MINUTE_IN_SECONDS);
    $still = volado_css_regen_verify($id);
    if ($still === '') {                                                       // healed -> purge that URL
        $url = get_permalink($id);
        if ($url && class_exists('\SiteGround_Optimizer\Supercacher\Supercacher') && method_exists('\SiteGround_Optimizer\Supercacher\Supercacher', 'purge_cache_request')) {
            try { \SiteGround_Optimizer\Supercacher\Supercacher::purge_cache_request($url); } catch (\Throwable $e) {}
        }
        update_option('volado_css_selfheal_log', $id . ' healed; was missing [' . $missing . '] @' . gmdate('c'), false);
    } else {
        update_option('volado_css_selfheal_log', $id . ' HEAL FAILED; still missing [' . $still . '] (cooldown 10m) @' . gmdate('c'), false);
    }
}, 5);

/* ---- C) REST/programmatic _elementor_data writes: regen (verified) + purge - */
/*        Not rate-limited: an explicit edit should always regenerate.         */
$volado_regen_on_meta = function ($meta_id, $post_id, $meta_key) {
    if ('_elementor_data' !== $meta_key || !class_exists('\Elementor\Plugin')) { return; }
    volado_css_regen_verify((int) $post_id);
    $url = get_permalink($post_id);
    if ($url && class_exists('\SiteGround_Optimizer\Supercacher\Supercacher') && method_exists('\SiteGround_Optimizer\Supercacher\Supercacher', 'purge_cache_request')) {
        try { \SiteGround_Optimizer\Supercacher\Supercacher::purge_cache_request($url); } catch (\Throwable $e) {}
    }
};
add_action('updated_post_meta', $volado_regen_on_meta, 10, 3);
add_action('added_post_meta', $volado_regen_on_meta, 10, 3);
