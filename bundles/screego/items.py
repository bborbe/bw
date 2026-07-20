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
    # Secret files owned by uid 1001 (the screego container user, USER 1001 in
    # bborbe/screego), mode 0600. The container runs non-root and bind-mounts
    # /data/screego, so the files must be readable by uid 1001 — root:root 0600
    # crashes it ("open /data/screego/users: permission denied"). Owning by the
    # service uid keeps them 0600 (not world-readable) AND readable by screego.
    # No host user maps to 1001, so owner/group are numeric.
    files['/data/screego/users'] = {
        'content': screego.get('users_file', ''),
        'owner': '1001',
        'group': '1001',
        'mode': '0600',
        'needs': ['directory:/data/screego'],
        'triggers': ['svc_systemd:screego:restart'],
    }
    files['/data/screego/environment'] = {
        'source': 'environment',
        'content_type': 'mako',
        'context': screego,
        'owner': '1001',
        'group': '1001',
        'mode': '0600',
        'needs': ['directory:/data/screego'],
        'triggers': ['svc_systemd:screego:restart'],
    }
    # Remove the legacy world-managed unit at /etc/systemd/system/, which shadows
    # this bundle's /lib unit (systemd prefers /etc). Left behind by the old
    # `world` tool; deleting it makes bw's unit authoritative.
    files['/etc/systemd/system/screego.service'] = {
        'delete': True,
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
    files['/etc/systemd/system/screego.service'] = {
        'delete': True,
    }
    files['/data/screego/environment'] = {
        'delete': True,
    }
    files['/data/screego/users'] = {
        'delete': True,
    }
