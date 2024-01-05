files = {}
svc_systemd = {}

if node.metadata.get('rancher-server', {}).get('enabled', False):
    svc_systemd['rancher-server'] = {
        'needs': [
            'file:/lib/systemd/system/rancher-server.service',
        ],
    }
    files['/lib/systemd/system/rancher-server.service'] = {
        'group': 'root',
        'mode': '0644',
        'needed_by': ['svc_systemd:rancher-server'],
        'owner': 'root',
        'source': 'rancher-server.service',
        'content_type': 'mako',
        'context': node.metadata.get('rancher-server', {}),
        'triggers': [
            'action:systemd-reload',
            'svc_systemd:rancher-server:restart',
        ],
    }
else:
    svc_systemd['rancher-server'] = {
        'running': False,
        'enabled': False,
    }
    files['/lib/systemd/system/rancher-server.service'] = {
        'delete': True,
    }
