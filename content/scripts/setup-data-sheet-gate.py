#!/usr/bin/env python3
"""Set up the gated rack data sheet on innovive.com. Volado Labs, 2026-10-16.

What it does, in order (each step is skipped if it is already done):
  1. HubSpot: creates two contact properties, data_sheet_requested (which sheet,
     from which page) and data_sheet_reason (what they need it for).
  2. HubSpot: creates the form "Data sheet request - info@innovive.com - Oct 2026"
     with the Contact Us fields Victoria asked for, the same notification
     recipients and consent text as Contact Us, and the two new properties.
  3. WordPress: adds the "Download data sheet" button to the Innorack Rat,
     Tall Rat and Tall Rat XL pages, copied from the Innorack Mouse page.
  4. WordPress: installs content/snippets/data-sheet-gate.php as an active
     Code Snippet, with the new form's id filled in.
  5. Clears the SiteGround cache (snippet #10) so visitors see it.

Run without arguments for a dry run that changes nothing:
    python3 content/scripts/setup-data-sheet-gate.py
Then for real:
    python3 content/scripts/setup-data-sheet-gate.py --apply

Credentials come from Bitwarden Secrets Manager (bwsx) and are never printed.
Every page is backed up to content/backups/ before it is changed.
"""
import base64, copy, datetime, json, pathlib, re, secrets, subprocess, sys, urllib.error, urllib.request

APPLY = '--apply' in sys.argv
REPO = pathlib.Path(__file__).resolve().parents[2]
BACKUPS = REPO / 'content' / 'backups'
SNIPPET_FILE = REPO / 'content' / 'snippets' / 'data-sheet-gate.php'
TODAY = datetime.date.today().isoformat()

PDF = 'https://innovive.com/wp-content/uploads/2026/06/innorack-data-sheets.pdf'
CONTACT_FORM = '4207ae0e-805c-44ba-a074-adf07bf26125'
FORM_NAME = 'Data sheet request - info@innovive.com - Oct 2026'
SNIPPET_NAME = 'Data sheet gate - rack data sheets ask for contact details first'
SOURCE_PAGE, SOURCE_BUTTON = 2677, 'aef6653'           # Innorack Mouse
# page id -> the Product Specifications container the button goes at the end of
TARGETS = {3067: 'e013aee', 2025: 'df22314', 2522: '4553d26'}
PAGE_NAMES = {3067: 'Innorack Rat', 2025: 'Tall Rat', 2522: 'Tall Rat XL'}


def bws(secret_id):
    out = subprocess.check_output([str(pathlib.Path.home() / '.local/bin/bwsx'), 'secret', 'get', secret_id, '-o', 'json'])
    return json.loads(out)['value']


def http(method, url, headers, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={**headers, 'Content-Type': 'application/json', 'User-Agent': 'volado-setup'})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            raw = r.read()
            try:
                return r.status, (json.loads(raw) if raw else None)
            except ValueError:
                # WordPress sometimes prefixes or replaces the JSON with stray output
                # (e.g. a PHP notice); keep the text so the caller can decide.
                return r.status, raw.decode(errors='replace')[:1500]
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode(errors='replace')[:1500]


HS = {'Authorization': 'Bearer ' + bws('e8754f83-9031-48aa-a3c0-b4ac003e6a9c')}
WP_PW = bws('66fa5fed-cc40-4660-989f-b49d0058d997').replace(' ', '')
WP = {'Authorization': 'Basic ' + base64.b64encode(f'voladoadmin:{WP_PW}'.encode()).decode()}


def hs(method, path, body=None):
    return http(method, 'https://api.hubapi.com/' + path, HS, body)


def wp(method, path, body=None):
    return http(method, 'https://innovive.com/wp-json/' + path, WP, body)


def step(msg):
    print(('APPLY  ' if APPLY else 'DRYRUN ') + msg)


def must(status, body, what):
    if status >= 300:
        sys.exit(f'FAILED {what}: HTTP {status} {body}')
    return body


# ---------------------------------------------------------------- 1. properties
PROPS = [
    {'name': 'data_sheet_requested', 'label': 'Data sheet requested', 'type': 'string', 'fieldType': 'text',
     'groupName': 'contactinformation',
     'description': 'Which data sheet the contact asked for on innovive.com, and the page they asked from. Set by the gated data sheet form (Volado, 2026-10-16).'},
    {'name': 'data_sheet_reason', 'label': 'Reason for requesting the data sheet', 'type': 'string', 'fieldType': 'textarea',
     'groupName': 'contactinformation',
     'description': 'What the contact said they need the data sheet for. Set by the gated data sheet form (Volado, 2026-10-16).'},
]
for p in PROPS:
    s, _ = hs('GET', f"crm/v3/properties/contacts/{p['name']}")
    if s == 200:
        step(f"property {p['name']} already exists")
        continue
    step(f"create contact property {p['name']}")
    if APPLY:
        must(*hs('POST', 'crm/v3/properties/contacts', p), f"create property {p['name']}")

# ---------------------------------------------------------------- 2. the form
contact = must(*hs('GET', f'marketing/v3/forms/{CONTACT_FORM}'), 'read Contact Us form')
form_id = None
s, lst = hs('GET', 'marketing/v3/forms?limit=100&formTypes=hubspot')
if s == 200:
    for f in lst.get('results', []):
        if f.get('name') == FORM_NAME:
            form_id = f['id']
if form_id:
    step(f'form already exists: {form_id}')
else:
    def field(name, label, ftype, required=False, hidden=False, **extra):
        return {'objectTypeId': '0-1', 'name': name, 'label': label, 'required': required, 'hidden': hidden, 'fieldType': ftype, **extra}

    def group(*fields):
        return {'groupType': 'default_group', 'richTextType': 'text', 'fields': list(fields)}

    cfg = copy.deepcopy(contact['configuration'])
    cfg.pop('embedType', None)   # let HubSpot pick; step 4 checks which embed it needs
    cfg['postSubmitAction'] = {'type': 'thank_you', 'value':
        f'<p>Thank you. <a href="{PDF}" target="_blank" rel="noopener">Download the Innorack data sheet</a>.</p>'}
    spec = {
        'name': FORM_NAME,
        'formType': 'hubspot',
        'archived': False,
        # The v3 create endpoint requires createdAt even though HubSpot sets it.
        'createdAt': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.000Z'),
        'fieldGroups': [
            group(field('firstname', 'First name', 'single_line_text', required=True),
                  field('lastname', 'Last name', 'single_line_text', required=True)),
            # HubSpot rejects email and phone fields without a validation block
            # ("Some required fields were not set: [validation]"); these match Contact Us.
            group(field('email', 'Email', 'email', required=True,
                        validation={'blockedEmailDomains': [], 'useDefaultBlockList': False})),
            group(field('phone', 'Phone number', 'phone', useCountryCodeSelect=False,
                        validation={'minAllowedDigits': 7, 'maxAllowedDigits': 20})),
            group(field('company', 'Company or institution', 'single_line_text', required=True)),
            group(field('data_sheet_reason', 'What are you planning? (optional)', 'multi_line_text')),
            group(field('data_sheet_requested', 'Data sheet requested', 'single_line_text', hidden=True)),
        ],
        'configuration': cfg,
        'displayOptions': {**contact['displayOptions'], 'submitButtonText': 'Get the data sheet'},
        'legalConsentOptions': contact['legalConsentOptions'],
    }
    print('       recipients copied from Contact Us:', cfg.get('notifyRecipients'))
    step(f'create HubSpot form "{FORM_NAME}"')
    if APPLY:
        form_id = must(*hs('POST', 'marketing/v3/forms', spec), 'create form')['id']
        print('       form id', form_id)

# Which embed does it need? The legacy endpoint only serves legacy-editor forms.
embed = 'v2'
if form_id:
    # Ask HubSpot directly: API-created forms come back as embedType V3 (legacy),
    # which only the v2 embed renders. The v4 embed leaves a legacy form at 0px,
    # which is what happened on 2026-10-16 when this check probed the legacy
    # endpoint and misread its reply.
    _, f = hs('GET', f'marketing/v3/forms/{form_id}')
    embed = 'v4' if isinstance(f, dict) and f.get('configuration', {}).get('embedType') == 'V4' else 'v2'
    print('       embed type:', embed)

# ---------------------------------------------------------------- 3. buttons
src = must(*wp('GET', f'wp/v2/pages/{SOURCE_PAGE}?context=edit&_fields=meta'), 'read Innorack Mouse page')
src_data = json.loads(src['meta']['_elementor_data'])


def find(els, eid):
    for e in els:
        if e['id'] == eid:
            return e
        hit = find(e.get('elements', []), eid)
        if hit:
            return hit
    return None


template = find(src_data, SOURCE_BUTTON)
if not template or PDF not in json.dumps(template):
    sys.exit('FAILED: the Innorack Mouse data sheet button has moved or changed; stop and look')

for pid, container_id in TARGETS.items():
    page = must(*wp('GET', f'wp/v2/pages/{pid}?context=edit&_fields=id,modified,meta'), f'read page {pid}')
    raw = page['meta']['_elementor_data']
    if PDF in raw:
        step(f'{PAGE_NAMES[pid]} ({pid}) already links the data sheet')
        continue
    data = json.loads(raw)
    box = find(data, container_id)
    if not box:
        sys.exit(f'FAILED: container {container_id} not found on page {pid}')
    used = set(re.findall(r'"id":"([0-9a-f]{7,8})"', raw.replace(' ', '')))
    btn = copy.deepcopy(template)
    while True:
        btn['id'] = secrets.token_hex(4)[:7]
        if btn['id'] not in used:
            break
    box['elements'].append(btn)
    step(f'add "Download data sheet" button to {PAGE_NAMES[pid]} ({pid}), end of container {container_id}')
    if APPLY:
        (BACKUPS / f'page-{pid}-{TODAY}-pre-data-sheet-button.json').write_text(json.dumps(page))
        new = json.dumps(data, separators=(',', ':'), ensure_ascii=True)
        must(*wp('POST', f'wp/v2/pages/{pid}?context=edit', {'meta': {'_elementor_data': new}}), f'save page {pid}')
        # The save reply is not always clean JSON (snippet #22 regenerates the page's
        # CSS during the request), so confirm by reading the page back.
        r = must(*wp('GET', f'wp/v2/pages/{pid}?context=edit&_fields=meta'), f're-read page {pid}')
        if PDF not in r['meta']['_elementor_data']:
            sys.exit(f'FAILED: page {pid} did not keep the new button')
        if r['meta'].get('_elementor_edit_mode') != 'builder':
            must(*wp('POST', f'wp/v2/pages/{pid}?context=edit', {'meta': {'_elementor_edit_mode': 'builder'}}), f'edit mode {pid}')

# ---------------------------------------------------------------- 4. snippet
code = SNIPPET_FILE.read_text()
code = re.sub(r'^<\?php\s*', '', code)
if APPLY and not form_id:
    sys.exit('FAILED: no form id, refusing to install the snippet')
code = code.replace('__FORM_GUID__', form_id or '__FORM_GUID__').replace('__EMBED__', embed)
s, snips = wp('GET', 'code-snippets/v1/snippets')
existing = [x for x in (snips if s == 200 else []) if x.get('name') == SNIPPET_NAME]
if existing:
    step(f"snippet already installed as #{existing[0]['id']} (active={existing[0].get('active')})")
else:
    step('install Code Snippet "' + SNIPPET_NAME + '" (front-end, priority 22, active)')
    if APPLY:
        r = must(*wp('POST', 'code-snippets/v1/snippets', {'name': SNIPPET_NAME, 'code': code, 'scope': 'front-end',
                                                           'priority': 22, 'active': True,
                                                           'desc': 'Rack data sheet links open a HubSpot form first. Source: innovive repo content/snippets/data-sheet-gate.php'}),
                 'install snippet')
        print('       snippet id', r.get('id'), 'active', r.get('active'))

# ---------------------------------------------------------------- 5. cache
step('clear the SiteGround cache (re-run snippet #10)')
if APPLY:
    must(*wp('PUT', 'code-snippets/v1/snippets/10', {'active': True}), 'purge cache')

print('\nDone.' if APPLY else '\nDry run only. Nothing was changed. Re-run with --apply to make these changes.')
