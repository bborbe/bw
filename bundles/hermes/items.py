directories = {}
files = {}
svc_systemd = {}
actions = {}

hermes = node.metadata.get('hermes', {})
matrix = hermes.get('matrix', {})
brave = hermes.get('brave', {})
telegram = hermes.get('telegram', {})
user = hermes.get('user', 'hermes')
home = '/home/{}'.format(user)
hermes_dir = '{}/.hermes'.format(home)
credentials_file = '{}/bw-credentials.env'.format(hermes_dir)

# Hermes manages its own gateway lifecycle via a user-level systemd unit
# (~/.config/systemd/user/hermes-gateway.service, installed by the upstream
# installer / `hermes gateway service install`). A system-level
# /etc/systemd/system/hermes.service fights it: Hermes detects it as
# "legacy" on every update and prints a migrate-legacy warning, and the
# Hermes CLI (`hermes gateway restart/stop/run`) targets a different
# process than systemd.
#
# So bw does NOT manage /etc/systemd/system/hermes*.service. Instead:
#   - enable-linger on the hermes user so its user-systemd survives logout
#     (and starts at boot without anyone logging in)
#   - clean up any prior bw-installed legacy unit
if hermes.get('enabled', False):
    actions['hermes_enable_linger'] = {
        'command': 'loginctl enable-linger {}'.format(user),
        'unless': 'test "$(loginctl show-user {} -p Linger --value 2>/dev/null)" = yes'.format(user),
        'needs': [
            'user:{}'.format(user),
        ],
    }

# Clean up the prior system-level unit from earlier commits of this bundle.
# Stays on the disabled branch unconditionally so the cleanup happens even
# if hermes is later disabled on a node that previously had it.
files['/etc/systemd/system/hermes.service'] = {
    'delete': True,
}
svc_systemd['hermes'] = {
    'running': False,
    'enabled': False,
}

env_vars = {}

if hermes.get('enabled', False) and matrix.get('enabled', False):
    for field in ('homeserver', 'user_id', 'password'):
        # `is None` (not `not matrix.get(...)`) — the value can be a bw
        # Fault (lazy TeamVault ref). Truthy/`not` checks force resolution,
        # which fails in CI where TeamVault credentials aren't present.
        if matrix.get(field) is None:
            raise Exception(
                'hermes.matrix.{} required when matrix.enabled on {}'.format(field, node.name)
            )
    env_vars['MATRIX_HOMESERVER'] = matrix['homeserver']
    # Hermes expects MATRIX_USER (not MATRIX_USER_ID — that's the openclaw
    # convention). Different agents, different env-var names. Do not "fix".
    env_vars['MATRIX_USER'] = matrix['user_id']
    env_vars['MATRIX_PASSWORD'] = matrix['password']

if hermes.get('enabled', False) and brave.get('enabled', False):
    # `is None` — see same comment above re: bw Fault / TeamVault resolution.
    if brave.get('api_key') is None:
        raise Exception(
            'hermes.brave.api_key required when brave.enabled on {}'.format(node.name)
        )
    env_vars['BRAVE_SEARCH_API_KEY'] = brave['api_key']

if hermes.get('enabled', False) and telegram.get('enabled', False):
    # `is None` — see same comment above re: bw Fault / TeamVault resolution.
    if telegram.get('bot_token') is None:
        raise Exception(
            'hermes.telegram.bot_token required when telegram.enabled on {}'.format(node.name)
        )
    if telegram.get('allowed_users') is None:
        # Required-by-bw policy: open Telegram bots on a public bot API let
        # anyone with the bot's username DM and command it. Force an
        # allowlist; set to "" only if open access is genuinely intentional.
        raise Exception(
            'hermes.telegram.allowed_users required when telegram.enabled on {} '
            '(set to "" to opt into open access)'.format(node.name)
        )
    env_vars['TELEGRAM_BOT_TOKEN'] = telegram['bot_token']
    env_vars['TELEGRAM_ALLOWED_USERS'] = telegram['allowed_users']

if env_vars:
    directories[hermes_dir] = {
        'owner': user,
        'group': user,
        'mode': '0700',
        'needs': [
            'user:{}'.format(user),
        ],
    }
    files[credentials_file] = {
        'source': 'env',
        'content_type': 'mako',
        'mode': '0600',
        'owner': user,
        'group': user,
        'context': {
            'env': env_vars,
        },
        'needs': [
            'directory:{}'.format(hermes_dir),
        ],
    }
else:
    files[credentials_file] = {
        'delete': True,
    }
