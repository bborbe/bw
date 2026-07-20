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
    # Secret files owned by the 'screego' service user (uid 1001 — matches the
    # container's USER in screego/server), mode 0600. The container runs non-root
    # and bind-mounts /data/screego, so files must be readable by uid 1001 —
    # root:root 0600 crashes it ("open /data/screego/users: permission denied").
    # Owning by the service user keeps them 0600 (not world-readable) AND readable
    # by screego. group root is fine (group bit is 0 at 0600). The 'screego' user
    # is created by the user bundle (see nodes/hz.hetzner-1.py 'users' metadata),
    # so a bare uid resolves to a name and bw converges.
    files['/data/screego/users'] = {
        'content': screego.get('users_file', ''),
        'owner': 'screego',
        'group': 'root',
        'mode': '0600',
        'needs': ['directory:/data/screego', 'user:screego'],
        'triggers': ['svc_systemd:screego:restart'],
    }
    files['/data/screego/environment'] = {
        'source': 'environment',
        'content_type': 'mako',
        'context': screego,
        'owner': 'screego',
        'group': 'root',
        'mode': '0600',
        'needs': ['directory:/data/screego', 'user:screego'],
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
