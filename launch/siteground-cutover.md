# SiteGround Go-Live Checklist — Innovive (inno.myvoladolabs.com → innovive.com)

The site is on SiteGround (hosting account `u2-j8oi65hzgyvy`). Steps grouped by phase. Most are done in **Site Tools**.

> **STATUS (2026-07-06): LIVE.** innovive.com is live over HTTPS with valid SSL. Done: DNS cutover, SSL (#7), 301 redirects (#8, snippet-based, 66 rules), Elementor cache flush, verification (#11). Remaining: GSC DNS TXT verify + sitemap (#10), confirm GA4 Realtime, optional SiteGround Dynamic Cache flush.

## BEFORE cutover
1. **Full manual backup** — Site Tools → Security → Backups → "Create Backup." (Also confirm auto-backups are on.)
2. **Add innovive.com to this site.** The site currently answers on `inno.myvoladolabs.com`. To serve `innovive.com` you either (a) add innovive.com to this SiteGround site and set it **Primary Domain**, or (b) migrate the install to the innovive.com hosting slot. Confirm which SiteGround account/site owns innovive.com.
3. **Lower DNS TTL** on innovive.com's current records to 300s ~24h before cutover, so propagation is fast.
4. **Uncheck "Discourage search engines"** — WordPress → Settings → Reading. Staging is usually set to noindex; the live site MUST have this OFF or Google won't index it. (Verify the live `<head>` has no site-wide `noindex` after go-live.)

## AT cutover (DNS — your standby person)

> **CRITICAL — email is on Google Workspace.** As of 2026-07-06, innovive.com DNS is at **Register.com** (`dns101/102.register.com`), email is **Google Workspace** (`aspmx.l.google.com` MX records), website is Wix (A `185.230.63.107`). Do NOT blindly switch to SiteGround nameservers — that moves ALL DNS to SiteGround and **kills @innovive.com email** unless the Google MX + SPF/DKIM records are recreated there first.
>
> **Preferred (Option A — A-record only):** keep DNS at Register.com; change ONLY the `@` A record → SiteGround server IP and `www` → same. Email/MX untouched. Lowest risk.
> **Option B (nameservers to SiteGround):** only after exporting the Register.com zone and recreating every record — especially Google Workspace MX + SPF/DKIM/DMARC TXT — in SiteGround DNS.

5. **Migrate FIRST, DNS LAST.** Complete the SiteGround Migrator transfer, verify the site on SiteGround's temporary URL, THEN change DNS (Option A preferred).
   - **SiteGround server IP (A-record target): `34.174.250.140`** (from destination Site Tools → Site, confirmed 2026-07-06 while migration in progress).
   - **Prerequisite:** confirm `innovive.com` is added to this SiteGround site (Site Tools → Domain) before pointing the A record, or the server won't serve the right site.
   - Then: `@` A → 34.174.250.140, `www` → same, at Register.com. Leave nameservers + MX untouched.
6. **Update the WordPress site URL** from `https://inno.myvoladolabs.com` → `https://innovive.com`:
   - Settings → General (Site Address + WordPress Address), AND
   - **Run a database search-replace** for `inno.myvoladolabs.com` → `innovive.com` (WP-CLI `search-replace` or the "Better Search Replace" plugin) — this is REQUIRED because Elementor stores absolute URLs in its data (images, links, backgrounds). Skipping this breaks images/links.
7. **Issue SSL** — once innovive.com resolves to SiteGround: Site Tools → Security → SSL Manager → install Let's Encrypt for innovive.com + www, then enable **HTTPS Enforce**.

## AFTER cutover
8. **Implement the 301 redirects** — use `launch/redirects.htaccess` (91 rules, place above `# BEGIN WordPress` in the site's .htaccess), OR Site Tools → Domain → Redirects, OR the "Redirection" plugin (CSV import of `launch/redirect-map.csv`). Review the `category-fallback` rows first (per-model old product pages → nearest category).
9. **Flush ALL caches** — Site Tools → Speed → Caching → flush **Dynamic Cache** AND **Memcached**, plus Elementor cache (WP → Elementor → Tools → Regenerate CSS & Data). NOTE: SiteGround's full-page Dynamic Cache is why edits can appear "stale" to logged-out visitors — always flush after changes.
10. **SEO/analytics live:**
    - Verify the GSC domain property `sc-domain:innovive.com` (add the DNS TXT record — your DNS person; token is in GSC → Settings → Ownership verification).
    - Submit the sitemap (`https://innovive.com/sitemap_index.xml`) in GSC.
    - Confirm GA4 tag firing on the live domain; connect GA4 ↔ GSC.
11. **Verify:** homepage + top pages load on innovive.com over HTTPS, images render (search-replace worked), a few 301s resolve, contact/InnoPlus forms submit and deliver.

## Notes / gotchas
- SiteGround's WAF blocks aggressive automated requests (it 403'd my scripted hits to `/contact/` — real browsers are unaffected). If bulk tools misbehave post-launch, that's why.
- Old innovive.com is a **Wix** site — DNS cutover replaces it entirely. Make sure email (MX) for @innovive.com is preserved through the DNS change.
- After go-live, update project CLAUDE.md REST base URL to innovive.com and consider rotating the staging app password.
