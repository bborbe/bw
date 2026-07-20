directories = {}
files = {}
svc_systemd = {}

screego = node.metadata.get('screego', {})

if screego.get('enabled', False):
    directories['/data/screego'] = {
        'owner': 'root',
        'group': 'root',
        'mode': '0755',
    }
    # Users file: "<name>:<bcrypt-hash>" lines. Sourced from TeamVault (node metadata).
    # 0600 — bcrypt hashes must not be world-readable (root reads them).
    files['/data/screego/users'] = {
        'content': screego.get('users_file', ''),
        'owner': 'root',
        'group': 'root',
        'mode': '0600',
        'needs': ['directory:/data/screego'],
        'triggers': ['svc_systemd:screego:restart'],
    }
    # 0600 — holds SCREEGO_SECRET (HMAC key); root-only.
    files['/data/screego/environment'] = {
        'source': 'environment',
        'content_type': 'mako',
        'context': screego,
        'owner': 'root',
        'group': 'root',
        'mode': '0600',
        'needs': ['directory:/data/screego'],
        'triggers': ['svc_systemd:screego:restart'],
    }
    files['/lib/systemd/system/screego.service'] = {
        'source': 'screego.service',
        'content_type': 'mako',
        'context': screego,
        'owner': 'root',
        'group': 'root',
        'mode': '0644',
        'needed_by': ['svc_systemd:screego'],
        'triggers': [
            'action:systemd-reload',
            'svc_systemd:screego:restart',
        ],
    }
    svc_systemd['screego'] = {
        'needs': [
            'file:/lib/systemd/system/screego.service',
            'file:/data/screego/environment',
            'file:/data/screego/users',
            'directory:/data/screego',
        ],
    }
else:
    svc_systemd['screego'] = {
        'running': False,
        'enabled': False,
    }
    files['/lib/systemd/system/screego.service'] = {
        'delete': True,
    }
    files['/data/screego/environment'] = {
        'delete': True,
    }
    files['/data/screego/users'] = {
        'delete': True,
    }
