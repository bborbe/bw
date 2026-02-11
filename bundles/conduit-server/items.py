directories = {}
files = {}
svc_systemd = {}

if node.metadata.get('conduit-server', {}).get('enabled', False):
    directories['/opt/conduit'] = {
        'owner': 'root',
        'group': 'root',
        'mode': '0755',
    }
    files['/opt/conduit/conduit.toml'] = {
        'group': 'root',
        'mode': '0644',
        'owner': 'root',
        'source': 'conduit.toml',
        'content_type': 'mako',
        'context': node.metadata.get('conduit-server', {}),
        'triggers': [
            'svc_systemd:conduit-server:restart',
        ],
        'needs': [
            'directory:/opt/conduit',
        ],
    }
    svc_systemd['conduit-server'] = {
        'needs': [
            'file:/lib/systemd/system/conduit-server.service',
            'file:/opt/conduit/conduit.toml',
            'directory:/opt/conduit',
        ],
    }
    files['/lib/systemd/system/conduit-server.service'] = {
        'group': 'root',
        'mode': '0644',
        'needed_by': ['svc_systemd:conduit-server'],
        'owner': 'root',
        'source': 'conduit-server.service',
        'content_type': 'mako',
        'context': node.metadata.get('conduit-server', {}),
        'triggers': [
            'action:systemd-reload',
            'svc_systemd:conduit-server:restart',
        ],
    }
else:
    svc_systemd['conduit-server'] = {
        'running': False,
        'enabled': False,
    }
    files['/lib/systemd/system/conduit-server.service'] = {
        'delete': True,
    }
    files['/opt/conduit/conduit.toml'] = {
        'delete': True,
    }
