<?php
/**
 * Code Snippets #37, v3. Volado Labs, deployed 2026-09-08.
 *
 * innovive.com runs TWO different HubSpot form embeds, and they expose
 * submissions on two different channels. v3 binds both.
 *
 *  - v4 embed (js-na2.hsforms.net/forms/embed/246069906.js + div.hs-form-frame)
 *    on /contact/, /inno-plus/ and /job-application-form/.
 *    It talks to its iframe over a PRIVATE MessageChannel, so nothing reaches
 *    the host window. It exposes a bubbling CustomEvent instead:
 *    'hs-form-event:on-submission:success' with detail {formId, instanceId}.
 *
 *  - legacy v2 embed (js-na2.hsforms.net/forms/embed/v2.js + hbspt.forms.create)
 *    on /job-application/, which carries the HR form.
 *    It posts window messages {type:'hsFormCallback', eventName:'onFormSubmitted'}.
 *
 * Why v1 recorded zero events for six weeks, two independent faults:
 *   1. It only ever bound the v2 postMessage channel, so the v4 forms that carry
 *      essentially all the volume could never be seen.
 *   2. Its origin check required an hsforms/hubspot origin, but the v2 embed
 *      relays hsFormCallback from the PARENT page, so ev.origin is the site's
 *      own origin. Verified live 2026-09-08: seven hsFormCallback messages, all
 *      origin https://innovive.com. So even the one legacy page was rejected.
 *
 * Spoofing: neither channel carries a third-party origin we can lean on, so
 * v4 events are authenticated with HubSpotFormsV4.getFormFromEvent (returns
 * undefined for a fabricated instanceId) and legacy events are restricted to
 * same-origin plus a form GUID on the allowlist below. Note that any script
 * already running on the page could call gtag() directly regardless, so this
 * is parity with the previous posture, not a relaxation.
 *
 * Consent unchanged: emits only via window.gtag, which snippet #7 defines ONLY
 * after CookieYes analytics consent.
 *
 * v1 backup: content/backups/snippet-37-2026-09-08-pre-v2-customevent.json
 */
add_action('wp_head', function () {
	$host = isset($_SERVER['HTTP_HOST']) ? $_SERVER['HTTP_HOST'] : '';
	// Dormant off-production: only emit on the live innovive.com domain
	if (strpos($host, 'innovive.com') === false) { return; }
	echo <<<'HTML'
<!-- GA4 form tracking - HubSpot embedded forms.
     Binds BOTH embeds in use on this site: the v4 embed's bubbling CustomEvent
     and the legacy v2 embed's hsFormCallback window message. Neither is visible
     to GA4 Enhanced Measurement, which is why this snippet exists.
     Consent: emits only via window.gtag, which snippet #7 defines ONLY after
     CookieYes analytics consent. No consent => no gtag => nothing is sent. -->
<script>
(function(){
  var FORMS = {
    '4207ae0e-805c-44ba-a074-adf07bf26125': { name: 'Contact Us',      inquiry: true  },
    '28d17095-a476-4751-8acb-4f1137b51e76': { name: 'Inno+ Inquiry',   inquiry: true  },
    'b29ca828-5c74-4531-b8fd-b82386d3b162': { name: 'Job Application', inquiry: false }
  };

  // A single submission must never be counted twice if both channels ever
  // speak for the same form.
  var seen = {};
  function emit(id, allowUnknown){
    if (!id) return;
    var now = Date.now();
    if (seen[id] && (now - seen[id]) < 5000) return;

    var cfg = FORMS[id];
    if (!cfg) {
      if (!allowUnknown) return;
      cfg = { name: 'Unknown form (' + id + ')', inquiry: true };
    }

    // No gtag means analytics consent was not given. Stay silent.
    if (typeof window.gtag !== 'function') return;
    seen[id] = now;

    // Inquiry forms and job applications are deliberately DIFFERENT events.
    // form_submit is the key event and must mean "someone enquired"; letting
    // job applications land in it would inflate the only conversion metric
    // the site has, which is the same mistake the CRM already makes.
    gtag('event', cfg.inquiry ? 'form_submit' : 'job_application', {
      form_id: id,
      form_name: cfg.name,
      page_path: location.pathname
    });
  }

  // --- Channel A: v4 embed, bubbling CustomEvent -------------------------
  window.addEventListener('hs-form-event:on-submission:success', function(ev){
    try {
      var id = String((ev.detail && ev.detail.formId) || '');
      if (!id) return;
      // Only HubSpot's own embed produces an event that resolves to a live
      // form instance. A fabricated CustomEvent resolves to undefined.
      try {
        if (window.HubSpotFormsV4 &&
            typeof window.HubSpotFormsV4.getFormFromEvent === 'function' &&
            !window.HubSpotFormsV4.getFormFromEvent(ev)) { return; }
      } catch (e) { /* fall through rather than lose a real conversion */ }
      emit(id, true);
    } catch (e) { /* never let tracking break the page */ }
  }, false);

  // --- Channel B: legacy v2 embed, hsFormCallback window message ----------
  window.addEventListener('message', function(ev){
    try {
      // The v2 embed relays this from the parent page, so the origin is our
      // own. Accept that, and an hsforms origin, and nothing else.
      var ok = (ev.origin === window.location.origin);
      if (!ok) {
        try {
          var h = new URL(ev.origin).hostname;
          ok = /(^|\.)hsforms\.net$/.test(h) || /(^|\.)hsforms\.com$/.test(h)
            || /(^|\.)hubspot\.com$/.test(h) || /(^|\.)hubapi\.com$/.test(h);
        } catch (e) { return; }
      }
      if (!ok) return;

      var d = ev.data;
      if (typeof d === 'string') { try { d = JSON.parse(d); } catch (e) { return; } }
      if (!d || d.type !== 'hsFormCallback' || d.eventName !== 'onFormSubmitted') return;

      // Same-origin messages are forgeable by any script on the page, so the
      // legacy channel accepts allowlisted form GUIDs only.
      emit(String((d.data && d.data.formGuid) || d.id || ''), false);
    } catch (e) { /* never let tracking break the page */ }
  }, false);
})();
</script>
HTML;
}, 21);
