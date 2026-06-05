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
systemd_user_dir = '{}/.config/systemd/user'.format(home)
dropin_dir = '{}/hermes-gateway.service.d'.format(systemd_user_dir)
dropin_file = '{}/bw-credentials.conf'.format(dropin_dir)

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

    # Systemd user-level drop-in that adds EnvironmentFile= to Hermes's
    # own ~/.config/systemd/user/hermes-gateway.service. We don't write
    # the main unit (Hermes does); the drop-in is additive and survives
    # Hermes updates that regenerate the main unit.
    directories[systemd_user_dir] = {
        'owner': user,
        'group': user,
        'mode': '0755',
        'needs': [
            'user:{}'.format(user),
        ],
    }
    directories[dropin_dir] = {
        'owner': user,
        'group': user,
        'mode': '0755',
        'needs': [
            'directory:{}'.format(systemd_user_dir),
        ],
    }
    files[dropin_file] = {
        'source': 'bw-credentials.conf',
        'content_type': 'mako',
        'mode': '0644',
        'owner': user,
        'group': user,
        'context': {
            'credentials_file': credentials_file,
        },
        'needs': [
            'directory:{}'.format(dropin_dir),
        ],
        'triggers': [
            'action:hermes_systemd_user_reload',
        ],
    }
    actions['hermes_systemd_user_reload'] = {
        # Run user-systemctl as the hermes user. Linger ensures a
        # persistent /run/user/<uid> runtime dir exists.
        'command': (
            'sudo -u {user} XDG_RUNTIME_DIR=/run/user/$(id -u {user}) '
            'systemctl --user daemon-reload && '
            'sudo -u {user} XDG_RUNTIME_DIR=/run/user/$(id -u {user}) '
            'systemctl --user restart hermes-gateway'
        ).format(user=user),
        'triggered': True,
        'needs': [
            'action:hermes_enable_linger',
        ],
    }
else:
    files[dropin_file] = {
        'delete': True,
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
        'triggers': [
            'action:hermes_systemd_user_reload',
        ],
    }
else:
    # Note: only trigger the systemd reload when hermes is enabled —
    # the action only exists in that branch. On disabled nodes we just
    # delete the file with no further effect.
    delete_creds = {'delete': True}
    if hermes.get('enabled', False):
        delete_creds['triggers'] = ['action:hermes_systemd_user_reload']
    files[credentials_file] = delete_creds
