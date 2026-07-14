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
    svc_systemd['lockbox'] = {
        'needs': [
            'file:/lib/systemd/system/lockbox.service',
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
else:
    svc_systemd['lockbox'] = {
        'running': False,
        'enabled': False,
    }
    files['/lib/systemd/system/lockbox.service'] = {
        'delete': True,
    }
