import bwtv as teamvault

files = {}
svc_systemd = {}
actions = {}

groups = {}
users = {}

if node.metadata.get('controller', {}).get('enabled', False):
    groups['controller'] = {}
    files['/lib/systemd/system/controller.service'] = {
        'group': 'root',
        'mode': '0644',
        'needed_by': ['svc_systemd:controller'],
        'owner': 'root',
        'source': 'controller.service',
        'content_type': 'mako',
        'context': {
            'token': teamvault.password('QL3QQw', site='benjamin-borbe'),
        },
        'triggers': [
            'action:systemd-reload',
            'svc_systemd:controller:restart',
        ],
    }

    svc_systemd['controller'] = {
        'needs': [
            'file:/lib/systemd/system/controller.service',
            'user:controller',
            'group:controller',
            'action:git_pull_hue',
            'action:install_golang',
        ],
    }

else:
    groups['controller'] = {
        'delete': True,
    }
    svc_systemd['controller'] = {
        'running': False,
        'enabled': False,
    }
    files['/opt/controller'] = {
        'delete': True,
    }
