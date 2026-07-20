svc_systemd = {}
files = {}

if node.metadata.get('ip', {}).get('enabled', False):
    svc_systemd['ip'] = {
        'needs': [
            'file:/lib/systemd/system/ip.service',
        ],
    }
    files['/lib/systemd/system/ip.service'] = {
        'group': 'root',
        'mode': '0644',
        'needed_by': ['svc_systemd:ip'],
        'owner': 'root',
        'source': 'ip.service',
        'content_type': 'mako',
        'context': node.metadata.get('ip', {}),
        'triggers': [
            'action:systemd-reload',
            'svc_systemd:ip:restart',
        ],
    }
else:
    svc_systemd['ip'] = {
        'running': False,
        'enabled': False,
    }
    files['/lib/systemd/system/ip.service'] = {
        'delete': True,
    }
