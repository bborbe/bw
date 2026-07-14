directories = {}
files = {}
svc_systemd = {}

if node.metadata.get('lockbox', {}).get('enabled', False):
    directories['/opt/lockbox'] = {
        'owner': 'root',
        'group': 'root',
        'mode': '0755',
    }
    directories['/opt/lockbox/data'] = {
        'owner': 'root',
        'group': 'root',
        'mode': '0755',
        'needs': [
            'directory:/opt/lockbox',
        ],
    }
    directories['/etc/lockbox'] = {
        'owner': 'root',
        'group': 'root',
        'mode': '0700',
    }
    svc_systemd['lockbox'] = {
        'needs': [
            'file:/lib/systemd/system/lockbox.service',
            'file:/etc/lockbox/lockbox.env',
            'directory:/opt/lockbox/data',
        ],
    }
    files['/lib/systemd/system/lockbox.service'] = {
        'group': 'root',
        'mode': '0644',
        'needed_by': ['svc_systemd:lockbox'],
        'owner': 'root',
        'source': 'lockbox.service',
        'content_type': 'mako',
        'context': node.metadata.get('lockbox', {}),
        'triggers': [
            'action:systemd-reload',
            'svc_systemd:lockbox:restart',
        ],
    }
    # Secrets live in a root-only 0600 env file, not inline in the
    # world-readable systemd unit (keeps them out of the unit file and
    # the `ps`/`docker inspect` cmdline). The content is built from the
    # TeamVault Faults and base64-encoded so BundleWrap diffs only the
    # content hash — the plaintext secrets never render in `bw apply -i`.
    _lb = node.metadata.get('lockbox', {})
    _env = (
        _lb['encryption_key'].format_into(
            "LISTEN=:8080\nDATADIR=/data\nLOCKBOX_ENCRYPTION_KEY={}\n"
        )
        + _lb['basic_auth_user'].format_into("BASIC_AUTH_USER={}\n")
        + _lb['basic_auth_pass'].format_into("BASIC_AUTH_PASS={}\n")
    )
    files['/etc/lockbox/lockbox.env'] = {
        'content': _env.b64encode(),
        'content_type': 'base64',
        'group': 'root',
        'mode': '0600',
        'needs': ['directory:/etc/lockbox'],
        'needed_by': ['svc_systemd:lockbox'],
        'owner': 'root',
        'triggers': [
            'svc_systemd:lockbox:restart',
        ],
    }
else:
    svc_systemd['lockbox'] = {
        'running': False,
        'enabled': False,
    }
    files['/lib/systemd/system/lockbox.service'] = {
        'delete': True,
    }
    files['/etc/lockbox/lockbox.env'] = {
        'delete': True,
    }
