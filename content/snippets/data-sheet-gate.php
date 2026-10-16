<?php
/**
 * Data sheet gate - rack data sheets ask for contact details first
 * (front-end, priority 22). Volado Labs, 2026-10-16.
 *
 * Asked for by Victoria on the 10/16 weekly sync: rack data sheets show cage
 * positions and rack sizes, so anyone downloading one is someone sales should
 * talk to. Consumable data sheets (metabolic cage) stay open for now, pending
 * Robin, because those readers are mostly current customers ordering parts.
 *
 * How it works: any click on a link to a GATED pdf opens a dialog with the
 * HubSpot "Data sheet request" form instead of the pdf. The form's hidden
 * data_sheet_requested field records which sheet and which page, so the info@
 * notification says what they wanted. After a successful submit the dialog
 * shows a download button.
 *
 * Nothing here is load-bearing for the page: if this snippet is off, or its
 * script fails, the same links simply download the pdf as before. That is also
 * why the pdf itself is not hidden. The gate asks, it does not lock; anyone
 * with the direct URL can still fetch the file, and that is deliberate.
 *
 * Embeds: the setup script fills EMBED with 'v2' (legacy editor form, rendered
 * by hbspt.forms.create) or 'v4' (new editor form, div.hs-form-frame), after
 * checking which kind HubSpot created. Both paths are below.
 *
 * Analytics: emits gtag 'data_sheet_request' only if window.gtag exists, which
 * snippet #7 defines only after CookieYes analytics consent. It is deliberately
 * NOT form_submit, so the site's inquiry key event keeps meaning "someone
 * enquired". Promote it in GA4 if Innovive wants it counted.
 *
 * Production only, like #7, #37 and #40: staging must never feed the live CRM.
 */
add_action('wp_head', function () {
	$host = isset($_SERVER['HTTP_HOST']) ? strtolower($_SERVER['HTTP_HOST']) : '';
	if ($host !== 'innovive.com' && $host !== 'www.innovive.com') { return; }
	echo <<<'HTML'
<!-- Data sheet gate (Volado Labs): rack data sheets open a short HubSpot form first. -->
<style>
#ivds-overlay{position:fixed;inset:0;z-index:999998;background:rgba(10,18,40,.55);display:none;align-items:center;justify-content:center;padding:16px}
#ivds-overlay.open{display:flex}
#ivds-dialog{background:#fff;border-radius:10px;max-width:560px;width:100%;max-height:calc(100vh - 32px);overflow:auto;padding:28px 28px 20px;position:relative;font-family:Inter,"Helvetica Neue",Helvetica,Arial,sans-serif;color:#242d28;box-shadow:0 20px 50px rgba(0,0,0,.25)}
#ivds-dialog h2{margin:0 36px 6px 0;font-size:22px;line-height:30px;color:#1b216b;font-weight:700}
#ivds-dialog p{margin:0 0 16px;font-size:15px;line-height:23px}
#ivds-close{position:absolute;top:12px;right:12px;width:36px;height:36px;border:0;background:transparent;font-size:26px;line-height:36px;cursor:pointer;color:#5a6472;border-radius:6px}
#ivds-close:hover,#ivds-close:focus{background:#f0f3f8}
#ivds-form iframe{width:100%!important;border:0}
#ivds-done{display:none}
#ivds-done a{display:inline-block;margin-top:4px;padding:12px 20px;background:#005287;color:#fcfbf8;border-radius:6px;font-weight:600;text-decoration:none}
</style>
<script>
(function(){
  'use strict';
  var PORTAL = '246069906', REGION = 'na2';
  var FORM_ID = '__FORM_GUID__';
  var EMBED = '__EMBED__';            // 'v2' or 'v4', set by the setup script
  // Path of each gated pdf -> the name staff will see in the notification.
  var GATED = {
    '/wp-content/uploads/2026/06/innorack-data-sheets.pdf': 'Innorack Data Sheet'
  };

  var overlay, dialog, formBox, done, doneLink, lastFocus, current = null, loaded = false;

  function gatedFor(a){
    try {
      var u = new URL(a.getAttribute('href'), location.href);
      if (u.hostname.replace(/^www\./,'') !== location.hostname.replace(/^www\./,'')) return null;
      return GATED[u.pathname] ? { name: GATED[u.pathname], href: u.href } : null;
    } catch (e) { return null; }
  }

  function requested(){
    return current ? current.name + ' | ' + location.pathname : location.pathname;
  }

  function build(){
    overlay = document.createElement('div');
    overlay.id = 'ivds-overlay';
    overlay.innerHTML =
      '<div id="ivds-dialog" role="dialog" aria-modal="true" aria-labelledby="ivds-title">' +
        '<button type="button" id="ivds-close" aria-label="Close">&times;</button>' +
        '<h2 id="ivds-title">Get the data sheet</h2>' +
        '<p>Tell us a little about you and your project, and the data sheet is yours right after.</p>' +
        '<div id="ivds-form"></div>' +
        '<div id="ivds-done" role="status"><p><strong>Thank you.</strong> Your data sheet is ready. Someone from our team may follow up to help with your project.</p>' +
        '<a id="ivds-link" href="#" target="_blank" rel="noopener">Download the data sheet</a></div>' +
      '</div>';
    document.body.appendChild(overlay);
    dialog = overlay.querySelector('#ivds-dialog');
    formBox = overlay.querySelector('#ivds-form');
    done = overlay.querySelector('#ivds-done');
    doneLink = overlay.querySelector('#ivds-link');
    overlay.querySelector('#ivds-close').addEventListener('click', close);
    overlay.addEventListener('click', function(e){ if (e.target === overlay) close(); });
    document.addEventListener('keydown', function(e){
      if (!overlay.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'Tab') {   // keep focus inside the dialog
        var f = dialog.querySelectorAll('button,a[href],input,select,textarea,iframe');
        if (!f.length) return;
        var first = f[0], last = f[f.length - 1];
        if (e.shiftKey && document.activeElement === first) { last.focus(); e.preventDefault(); }
        else if (!e.shiftKey && document.activeElement === last) { first.focus(); e.preventDefault(); }
      }
    });
  }

  function open(g){
    if (!overlay) build();
    current = g;
    lastFocus = document.activeElement;
    overlay.querySelector('#ivds-title').textContent = 'Get the ' + g.name;
    doneLink.href = g.href;
    done.style.display = 'none';
    formBox.style.display = '';
    overlay.classList.add('open');
    document.documentElement.style.overflow = 'hidden';
    overlay.querySelector('#ivds-close').focus();
    if (!loaded) { loaded = true; load(); }
    else setHidden();   // same page session, new sheet: refresh the hidden value
  }

  function close(){
    overlay.classList.remove('open');
    document.documentElement.style.overflow = '';
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  function success(){
    formBox.style.display = 'none';
    done.style.display = 'block';
    doneLink.focus();
    try {
      if (typeof window.gtag === 'function') {
        window.gtag('event', 'data_sheet_request', {
          form_id: FORM_ID, form_name: 'Data sheet request',
          data_sheet: current ? current.name : '', page_path: location.pathname
        });
      }
    } catch (e) {}
  }

  // --- hidden field --------------------------------------------------------
  var v2Form = null, v4Form = null;
  function setHidden(){
    var val = requested();
    try {
      if (v4Form && v4Form.setFieldValue) v4Form.setFieldValue('0-1/data_sheet_requested', val);
      if (v2Form) {
        var el = v2Form.querySelector('input[name="data_sheet_requested"]');
        if (el) { el.value = val; el.dispatchEvent(new Event('change', { bubbles: true })); }
      }
    } catch (e) {}
  }

  function inject(src, cb){
    var s = document.createElement('script');
    s.src = src; s.async = true; s.onload = cb;
    document.head.appendChild(s);
  }

  function load(){
    if (EMBED === 'v4') {
      formBox.innerHTML = '<div class="hs-form-frame" data-region="' + REGION + '" data-portal-id="' + PORTAL + '" data-form-id="' + FORM_ID + '"></div>';
      window.addEventListener('hs-form-event:on-ready', function(ev){
        try {
          if (!ev.detail || ev.detail.formId !== FORM_ID || !window.HubSpotFormsV4) return;
          v4Form = window.HubSpotFormsV4.getFormFromEvent(ev);
          setHidden();
        } catch (e) {}
      });
      window.addEventListener('hs-form-event:on-submission:success', function(ev){
        if (ev.detail && ev.detail.formId === FORM_ID) success();
      });
      if (!window.__hsf246069906) {
        window.__hsf246069906 = 1;
        inject('https://js-' + REGION + '.hsforms.net/forms/embed/' + PORTAL + '.js', function(){});
      }
      return;
    }
    // Legacy v2 embed.
    inject('https://js-' + REGION + '.hsforms.net/forms/embed/v2.js', function(){
      if (!window.hbspt) return;
      window.hbspt.forms.create({
        region: REGION, portalId: PORTAL, formId: FORM_ID, target: '#ivds-form',
        onFormReady: function(f){ v2Form = (f && f[0]) ? f[0] : f; setHidden(); },
        onFormSubmitted: success
      });
      // HubSpot's own auto-resize does not fire reliably on this site (seen on
      // /job-application/), so size the same-origin iframe to its content.
      var t = setInterval(function(){
        var fr = formBox.querySelector('iframe');
        try {
          if (fr && fr.contentDocument && fr.contentDocument.body) {
            fr.style.height = fr.contentDocument.body.scrollHeight + 'px';
          }
        } catch (e) { clearInterval(t); }
      }, 600);
    });
  }

  // Capture phase, so Elementor's own link handling never sees a gated click.
  document.addEventListener('click', function(e){
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    var a = e.target && e.target.closest ? e.target.closest('a[href]') : null;
    if (!a) return;
    var g = gatedFor(a);
    if (!g || FORM_ID.indexOf('__') === 0) return;
    e.preventDefault();
    open(g);
  }, true);
})();
</script>
HTML;
}, 22);
