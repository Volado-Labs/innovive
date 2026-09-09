<?php
$map = json_decode(base64_decode('eyJyYXQtbmVzdGluZy1zaGVldHMiOiAiL3JhdC1jYWdpbmcvIiwgInJhdC1jYXJkLWhvbGRlciI6ICIvcmF0LWNhZ2luZy8iLCAidGFsbC14bC1yYXQtY2FnaW5nLXItd2lyZS10ZCI6ICIvdGFsbC1yYXQteGwvIiwgIm1vdXNlLWFscGhhLWRyaS1wbHVzIjogIi9tb3VzZS1jYWdpbmcvIiwgIm1vdXNlLWNhZ2luZy1tdngyIjogIi9tb3VzZS1jYWdpbmcvIiwgInRhbGwteGwtcmF0LWNhZ2luZy1idG0iOiAiL3JhdC1jYWdpbmctYnRtLyIsICJ0YWxsLXhsLXJhdC1jYWdpbmctbGlkLXJ2eDcteGwiOiAiL3RhbGwtcmF0LXhsLyIsICJjb3JuLWNvYi1yYXQiOiAiL21vdXNlLXJhdC1iZWRkaW5nLyIsICJ0YWxsLXJhdC1jYWdpbmctYnRtIjogIi9yYXQtY2FnaW5nLWJ0bS8iLCAicmF0LXByb2R1Y3RzIjogIi9yYXQtcmFja3MvIiwgImFib3V0LXVzIjogIi9hYm91dC8iLCAibW91c2UtYmlvZnJlc2giOiAiL21vdXNlLWNhZ2luZy8iLCAicmF0LWxpZHMtcnN4MSI6ICIvcmF0LWxpZC8iLCAibW91c2UtY2FnaW5nLW12eDMiOiAiL21vdXNlLWNhZ2luZy8iLCAidGFsbC1yYXQtY2FnaW5nLWxpZC1ydng4IjogIi90YWxsLXJhdC0wMS8iLCAici13aXJlLWhiIjogIi9yYXQtY2FnaW5nLyIsICJ0YWxsLXhsLXJhdC1yYWNrIjogIi90YWxsLXJhdC14bC8iLCAiYmxvZyI6ICIvYmxvZy1uZXdzLyIsICJtb3VzZS1jYWdpbmctbXZ4MSI6ICIvbW91c2UtY2FnaW5nLyIsICJjYXN1cHBseWNoYWludHJhbnNwYXJhbmN5YWN0IjogIi9jYS1zdXBwbHktY2hhaW4vIiwgInJhdC1saWRzIjogIi9yYXQtbGlkLyIsICJjYXJlZXJzIjogIi9jYXJlZXIvIiwgInJhdC1jYWdpbmctbGlkLXJ2eDYiOiAiL3JhdC1jYWdpbmcvIiwgIm1vdXNlLWNhZ2luZy1jYXJkLWhvbGRlciI6ICIvbW91c2UtY2FnaW5nLyIsICJtb3VzZS1jb3JuLWNvYiI6ICIvbW91c2UtY2FnaW5nLyIsICJyYXQtbGlkcy1ydng2MiI6ICIvcmF0LWxpZC8iLCAicmF0LWxpZHMtcnZ4NSI6ICIvcmF0LWxpZC8iLCAibW91c2UtY2FnaW5nLW5lc3Rpbmctc2hlZXRzIjogIi9tb3VzZS1jYWdpbmcvIiwgIm1vdXNlLWNhZ2luZy1tc3gyIjogIi9tb3VzZS1jYWdpbmcvIiwgIm1vdXNlLWNhZ2luZy1pbm5vdHViZSI6ICIvbW91c2UtY2FnaW5nLyIsICJtb3VzZS1wcm9kdWN0cyI6ICIvaW5ub3JhY2stbW91c2UvIiwgInRhbGwtcmF0LWNhZ2luZy1saWQtcnZ4NyI6ICIvdGFsbC1yYXQtMDEvIiwgInItZmVlZC11IjogIi9yYXQtY2FnaW5nLyIsICJiaW9mcmVzaC1yYXQiOiAiL21vdXNlLXJhdC1iZWRkaW5nLyIsICJtb3VzZS1jYWdpbmctbXZ4NiI6ICIvbW91c2UtY2FnaW5nLyIsICJtb3VzZS1jYWdpbmctbS1mZWVkIjogIi9tb3VzZS1jYWdpbmcvIiwgImlubm92aXZlLXdhdGVyLXByb2Nlc3MiOiAiL3N1c3RhaW5hYmlsaXR5LyIsICJtb3VzZS10cmFuc3BvcnQtY2FydCI6ICIvbW91c2UtdHJhbnNwb3J0YXRpb24tY2FydC8iLCAicGF0ZW50cyI6ICIvcGF0ZW50cy0yLTIvIiwgInRhbGwteGwtcmF0LWNhZ2luZy1yLXdpcmUteGwiOiAiL3RhbGwtcmF0LXhsLyIsICJ0YWxsLXJhdC1yYWNrIjogIi90YWxsLXJhdC0wMS8iLCAibW91c2UtcmFja3MiOiAiL2lubm9yYWNrLW1vdXNlLyIsICJtb3VzZS1jYWdpbmctbS1jbGltYiI6ICIvbW91c2UtY2FnaW5nLyIsICJuZXdzIjogIi9ibG9nLW5ld3MvIiwgInRhbGwtcmF0LWxvZnQiOiAiL3RhbGwtcmF0LTAxLyIsICJyLXdpcmUtdGQiOiAiL3JhdC1jYWdpbmcvIiwgIm1vdXNlLWNhZ2luZy1tLWZlZWQtc3MiOiAiL21vdXNlLWNhZ2luZy8iLCAibW91c2UtY2FnaW5nLW0tZGl2aWRlcjIiOiAiL21vdXNlLWNhZ2luZy8iLCAidGVybXMtY29uZGl0aW9ucyI6ICIvdGVybXMtYW5kLWNvbmRpdGlvbnMvIiwgIm1vdXNlLWFscGhhLWRyaSI6ICIvbW91c2UtY2FnaW5nLyIsICJyLXdicCI6ICIvcmF0LWNhZ2luZy8iLCAibW91c2UtY2FnaW5nLXByb2R1Y3RzIjogIi9tb3VzZS1jYWdpbmcvIiwgImNvbnRhY3QtdXMiOiAiL2NvbnRhY3QvIiwgImdsb2JhbC1yZXByZXNlbnRhdGlvbiI6ICIvcmVnaW9uYWwtZGlzdHJpYnV0b3JzLyIsICJtb3VzZS1jYWdpbmctbS1mZWVkLXAiOiAiL21vdXNlLWNhZ2luZy8iLCAiYWxwaGEtZHJpLXJhdCI6ICIvbW91c2UtcmF0LWJlZGRpbmcvIiwgIm1vdXNlLWNhZ2luZy1tdng1IjogIi9tb3VzZS1jYWdpbmcvIiwgIm1vdXNlLWNhZ2luZy1pbm5vd2hlZWwiOiAiL21vdXNlLWNhZ2luZy8iLCAibW91c2UtY2FnaW5nLW1zeDQiOiAiL21vdXNlLWNhZ2luZy8iLCAibmV3cy9pbm5vdml2ZS1leHBhbmRzLWdsb2JhbC1yZWFjaC10aHJvdWdoLXN0cmF0ZWdpYy1wYXJ0bmVyc2hpcC13aXRoLWF0dGVudGl2ZS1zY2llbmNlLXRvLWFjY2VsZXJhdGUtc2NpZW50aWZpYy1yZXNlYXJjaC1hY3Jvc3MtZ2NjLWFuZC1tZW5hLXJlZ2lvbnMiOiAiL2Jsb2ctbmV3cy8iLCAibmV3cy9pbm5vdml2ZS1leHBhbmRzLWludG8tbGF0aW4tYW1lcmljYS1hbmQtY2FyaWJiZWFuIjogIi9ibG9nLW5ld3MvIiwgIm5ld3MvbmV3LWNoaWVmLWV4ZWN1dGl2ZS1vZmZpY2VyIjogIi9ibG9nLW5ld3MvIiwgIm5ld3Mvc3RyYXRlZ2ljLXBhcnRuZXJzaGlwLXdpdGgtZHItbWFyY2VsLXBlcnJldC1nZW50aWwiOiAiL2Jsb2ctbmV3cy8iLCAibmV3cy9tYWpvci1lbnZpcm9ubWVudGFsLW1pbGVzdG9uZXMiOiAiL2Jsb2ctbmV3cy8iLCAibmV3cy9wZXQtcm9kZW50LWNhZ2UtcHJvY2Vzc29yLXJlY3ljbGVkIjogIi9ibG9nLW5ld3MvIiwgIm5ld3MvcHJvZHVjdC1zdXBwb3J0LXNlcnZpY2VzLWFuZC12aXZhcml1bS1tYW5hZ2VtZW50LXNvbHV0aW9ucyI6ICIvYmxvZy1uZXdzLyIsICJjYXNlLXN0dWRpZXMtMi0yIjogIi9jYXNlLXN0dWRpZXMvIn0='), true);
// Hooked on 'wp' at priority 0: MUST run before other redirect handlers, or legacy paths
// that happen to collide with something WP can resolve never reach this map.
// Two real cases found 2026-09-09: (a) /r-wire-hb/, /r-feed-u/, /r-wire-td/ and
// /r-wbp/ are parentless MEDIA ATTACHMENTS whose permalink is exactly that path,
// and Rank Math's attachment redirect sent all four to the homepage; (b)
// /mouse-racks/ is a published WooCommerce product slug, so core's
// redirect_canonical (priority 10) sent it to /product/mouse-racks/.
// The map is an explicit allowlist of retired Wix paths, so winning the race for
// those exact paths is safe; every other request returns immediately.
add_action('wp', function() use ($map) {
  if (is_admin()) return;
  // Real News CPT posts were recreated at former Wix /news/ URLs — let WP serve them (don't legacy-redirect).
  if (is_singular('news')) return;
  $p = strtolower(trim(parse_url($_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH), '/'));
  if ($p==='' ) return;
  if (isset($map[$p])) { wp_redirect(home_url($map[$p]), 301); exit; }
}, 0);

// Retired duplicate pages. Kept separate from the Wix map above because this one
// is LANGUAGE-AWARE: TranslatePress publishes every page under /ar/ /de/ /es/ /fr/
// /ko/ /pt/ /zh/ too, and the Wix map matches the whole path so it only ever
// catches the root URL. Retiring a page means retiring all 8 of its URLs.
// Volado Labs 2026-09-08: /job-application-form/ (page 3965) duplicated
// /job-application/ (3268); both now carry the HR form, nothing linked to 3965.
//
// NOTE: strip the language prefix to do the lookup, but do NOT put it back.
// TranslatePress already filters home_url() to the current language, so
// re-adding it yields /ar/ar/... (observed live before this was corrected).
$volado_retired = array(
  'job-application-form' => 'job-application',
);
add_action('wp', function() use ($volado_retired) {
  if (is_admin()) return;
  $path = trim(parse_url($_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH), '/');
  if ($path === '') return;
  $seg = explode('/', strtolower($path));
  if (count($seg) > 1 && in_array($seg[0], array('ar','de','es','fr','ko','pt','zh'), true)) {
    array_shift($seg);
  }
  $slug = implode('/', $seg);
  if (isset($volado_retired[$slug])) {
    wp_redirect(home_url('/' . $volado_retired[$slug] . '/'), 301);
    exit;
  }
}, 0);
