<?php
/**
 * Snippet #40 — LinkedIn Insight Tag, consent-gated (front-end, priority 20)
 *
 * Mirrors snippet #7 exactly: host-gated to production so staging stays clean,
 * and emits nothing until CookieYes records consent for the category. The only
 * difference is the category, `advertisement` rather than `analytics`, because
 * the Insight Tag sets advertising cookies (li_fat_id, lms_ads,
 * UserMatchHistory, AnalyticsSyncHistory, li_sugr, bcookie).
 *
 * BEFORE ACTIVATING: replace 9263068 with the numeric partner ID from
 * LinkedIn Campaign Manager > Analyze > Insight Tag (or Account Assets >
 * Insight Tag). Account 514047946. It is 6 to 8 digits, no quotes needed
 * around the number in LinkedIn's own snippet but we keep it a string here so
 * a leading zero can never be dropped.
 *
 * Also activate snippet #39 first, which files the six LinkedIn cookies under
 * CookieYes's Advertisement category so the preference centre describes them
 * accurately. #39 is idempotent and self-disables via an option flag.
 */

add_action('wp_head', function () {
	$host = isset($_SERVER['HTTP_HOST']) ? $_SERVER['HTTP_HOST'] : '';
	// Dormant off-production: only emit on the live innovive.com domain
	if (strpos($host, 'innovive.com') === false) { return; }
	echo <<<'HTML'
<!-- LinkedIn Insight Tag - consent-gated: loads only after CookieYes advertisement consent -->
<script>
(function(){
  function a(c){try{var m=document.cookie.match(/cookieyes-consent=([^;]+)/);if(!m)return false;return new RegExp('(^|,)'+c+':yes(,|$)').test(decodeURIComponent(m[1]));}catch(e){return false;}}
  var done=false;
  function g(){if(done||!a('advertisement'))return;done=true;
    window._linkedin_partner_id='9263068';
    window._linkedin_data_partner_ids=window._linkedin_data_partner_ids||[];
    window._linkedin_data_partner_ids.push(window._linkedin_partner_id);
    if(!window.lintrk){window.lintrk=function(a,b){window.lintrk.q.push([a,b]);};window.lintrk.q=[];}
    var s=document.createElement('script');s.async=true;s.type='text/javascript';
    s.src='https://snap.licdn.com/li.lms-analytics/insight.min.js';
    document.head.appendChild(s);}
  g();
  document.addEventListener('cookieyes_consent_update',g);
})();
</script>
HTML;
}, 20);
