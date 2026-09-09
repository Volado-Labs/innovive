<?php
/**
 * PROPOSED replacement for Code Snippets #37, NOT YET DEPLOYED.
 * Volado Labs, 2026-09-08. Awaiting Collin's approval.
 *
 * Why: the deployed v1 listens for the LEGACY HubSpot v2 embed API,
 * window 'message' with {type:'hsFormCallback', eventName:'onFormSubmitted'}.
 * innovive.com runs the v4 embed (js-na2.hsforms.net/forms/embed/246069906.js),
 * which talks to its iframe over a PRIVATE MessageChannel and never posts a
 * window-level message to the host page. v1 therefore cannot fire, for anyone,
 * consented or not. Verified live on 2026-09-08: a full form render produced
 * ZERO window messages from any hsforms origin.
 *
 * The v4 embed instead dispatches bubbling DOM CustomEvents on the form
 * container: 'hs-form-event:on-submission:success' with detail {formId, instanceId}.
 * Snippet #38 (HubSpot UTM bridge, live since 2026-09-01) already uses this
 * exact event successfully, so the pattern is proven on this site.
 *
 * Spoofing: the v1 origin check is not available for CustomEvents, so we
 * authenticate via HubSpotFormsV4.getFormFromEvent(), which returns undefined
 * for a fabricated instanceId and a live form object for a genuine one
 * (verified 2026-09-08). Note that any script already executing on the page
 * could call gtag() directly regardless, so this is parity, not a downgrade.
 *
 * Consent behaviour is UNCHANGED: emits only via window.gtag, which snippet #7
 * defines ONLY after CookieYes analytics consent.
 */
add_action('wp_head', function () {
	$host = isset($_SERVER['HTTP_HOST']) ? $_SERVER['HTTP_HOST'] : '';
	// Dormant off-production: only emit on the live innovive.com domain
	if (strpos($host, 'innovive.com') === false) { return; }
	echo <<<'HTML'
<!-- GA4 form tracking - HubSpot v4 embedded forms.
     The v4 embed renders the form in a cross-origin iframe and communicates
     with it over a private MessageChannel, so neither GA4 Enhanced Measurement
     nor a window 'message' listener can observe a submission. The supported
     host-page hook is a bubbling CustomEvent, which is what we bind here.
     Consent: emits only via window.gtag, which snippet #7 defines ONLY after
     CookieYes analytics consent. No consent => no gtag => nothing is sent. -->
<script>
(function(){
  var FORMS = {
    '4207ae0e-805c-44ba-a074-adf07bf26125': { name: 'Contact Us',      inquiry: true  },
    '28d17095-a476-4751-8acb-4f1137b51e76': { name: 'Inno+ Inquiry',   inquiry: true  },
    'b29ca828-5c74-4531-b8fd-b82386d3b162': { name: 'Job Application', inquiry: false }
  };

  window.addEventListener('hs-form-event:on-submission:success', function(ev){
    try {
      var id = String((ev.detail && ev.detail.formId) || '');
      if (!id) return;

      // Only HubSpot's own embed can produce an event that resolves to a live
      // form instance. A fabricated CustomEvent resolves to undefined.
      try {
        if (window.HubSpotFormsV4 &&
            typeof window.HubSpotFormsV4.getFormFromEvent === 'function' &&
            !window.HubSpotFormsV4.getFormFromEvent(ev)) { return; }
      } catch (e) { /* fall through rather than lose a real conversion */ }

      // No gtag means analytics consent was not given. Stay silent.
      if (typeof window.gtag !== 'function') return;

      var cfg = FORMS[id] || { name: 'Unknown form (' + id + ')', inquiry: true };

      // Inquiry forms and job applications are deliberately DIFFERENT events.
      // form_submit is the key event and must mean "someone enquired"; letting
      // job applications land in it would inflate the only conversion metric
      // the site has, which is the same mistake the CRM already makes.
      gtag('event', cfg.inquiry ? 'form_submit' : 'job_application', {
        form_id: id,
        form_name: cfg.name,
        page_path: location.pathname
      });
    } catch (e) { /* never let tracking break the page */ }
  }, false);
})();
</script>
HTML;
}, 21);
