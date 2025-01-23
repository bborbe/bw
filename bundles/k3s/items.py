if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

files = {}
svc_systemd = {}
directories = {}

if node.metadata.get('k3s', {}).get('enabled', False):
    directories['/var/lib/rancher/k3s/storage'] = {
        'mode': '0700',
        'owner': 'root',
        'group': 'root',
    }

    svc_systemd['multipathd.service'] = {
        'running': False,
        'enabled': False,
    }
    svc_systemd['multipathd.socket'] = {
        'running': False,
        'enabled': False,
    }

    if node.metadata.get('k3s', {}).get('agent', False):
        svc_systemd['k3s-agent'] = {
            'running': True,
            'enabled': True,
            'needs': [
                'file:/etc/rancher/k3s/config.yaml',
                # 'file:/var/lib/rancher/k3s/server/manifests/local-path.yaml',
            ],
        }
        files['/etc/rancher/k3s/config.yaml'] = {
            'source': 'agent-config.yaml',
            'content_type': 'text',
            'mode': '0644',
            'owner': 'root',
            'group': 'root',
            'triggers': ['svc_systemd:k3s-agent:restart'],
        }
    else:
        svc_systemd['k3s'] = {
            'running': True,
            'enabled': True,
            'needs': [
                'file:/etc/rancher/k3s/config.yaml',
                # 'file:/var/lib/rancher/k3s/server/manifests/local-path.yaml',
            ],
        }
        files['/etc/rancher/k3s/config.yaml'] = {
            'source': 'master-config.yaml',
            'content_type': 'text',
            'mode': '0644',
            'owner': 'root',
            'group': 'root',
            'triggers': ['svc_systemd:k3s:restart'],
        }
    # files['/var/lib/rancher/k3s/server/manifests/local-path.yaml'] = {
    #     'source': 'local-path.yaml',
    #     'content_type': 'text',
    #     'mode': '0600',
    #     'owner': 'root',
    #     'group': 'root',
    #     'triggers': ['svc_systemd:k3s:restart'],
    # }
else:
    files['/etc/rancher/k3s/master-config.yaml'] = {
        'delete': True,
    }
    # files['/var/lib/rancher/k3s/server/manifests/local-path.yaml'] = {
    #     'delete': True,
    # }
    svc_systemd['k3s'] = {
        'running': False,
        'enabled': False,
    }
    svc_systemd['k3s-agent'] = {
        'running': False,
        'enabled': False,
    }
