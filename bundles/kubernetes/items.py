os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if os != 'ubuntu' or release != 'xenial':
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

files = {}

pkg_apt = {
    'kubelet': {
        'installed': node.metadata.get('kubernetes', {}).get('enabled', False),
    },
    'kubeadm': {
        'installed': node.metadata.get('kubernetes', {}).get('enabled', False),
    },
    'kubectl': {
        'installed': node.metadata.get('kubernetes', {}).get('enabled', False),
    },
    'kubernetes-cni': {
        'installed': node.metadata.get('kubernetes', {}).get('enabled', False),
    },
}

actions = {}

if node.metadata.get('kubernetes', {}).get('enabled', False):
    actions['kube_init'] = {
        'command': 'rm -rf /var/lib/kubelet/*; rm -rf /var/lib/etcd/*; kubeadm init --use-kubernetes-version {version}'.format(version='v1.4.6'),
        'unless': 'test -e /etc/kubernetes/admin.conf',
        'needs': ['pkg_apt:kubelet', 'pkg_apt:kubeadm'],
    }
    svc_systemd = {
        'kubelet': {
            'running': True,
            'enabled': True,
            'needs': ['pkg_apt:kubelet', 'action:kube_init'],
        },
    }
else:
    svc_systemd = {
        'kubelet': {
            'running': False,
            'enabled': False,
        },
    }

if node.metadata.get('kubernetes', {}).get('enabled', False):
    files['/etc/systemd/system/kubelet.service.d/10-kubeadm.conf'] = {
        'source': '10-kubeadm.conf',
        'content_type': 'text',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'needs': ['pkg_apt:kubelet'],
        'triggers': [
            'action:systemd-reload',
            'svc_systemd:kubelet:restart'
        ],
    }
else:
    files['/etc/systemd/system/kubelet.service.d/10-kubeadm.conf'] = {
        'delete': True,
    }
