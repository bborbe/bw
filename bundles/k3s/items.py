if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

files = {}
svc_systemd = {}
directories = {}

if node.metadata.get('k3s', {}).get('enabled', False):
    directories['/var/lib/rancher/k3s/storage'] = {
        'mode': '0755',
        'owner': 'root',
        'group': 'root',
    }
    directories['/var/lib/rancher/k3s/storage/hdd'] = {
        'mode': '0700',
        'owner': 'root',
        'group': 'root',
    }
    directories['/var/lib/rancher/k3s/storage/ssd'] = {
        'mode': '0700',
        'owner': 'root',
        'group': 'root',
    }
    svc_systemd['k3s'] = {
        'running': True,
        'enabled': True,
        'needs': [
            'file:/etc/rancher/k3s/config.yaml',
            'file:/var/lib/rancher/k3s/server/manifests/local-path.yaml',
        ],
    }
    files['/etc/rancher/k3s/config.yaml'] = {
        'source': 'config.yaml',
        'content_type': 'text',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'triggers': ['svc_systemd:k3s:restart'],
    }
    files['/var/lib/rancher/k3s/server/manifests/local-path.yaml'] = {
        'source': 'local-path.yaml',
        'content_type': 'text',
        'mode': '0600',
        'owner': 'root',
        'group': 'root',
        'triggers': ['svc_systemd:k3s:restart'],
    }
else:
    files['/etc/rancher/k3s/config.yaml'] = {
        'delete': True,
    }
    svc_systemd['k3s'] = {
        'running': False,
        'enabled': False,
    }
