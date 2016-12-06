os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if os != 'ubuntu' or release != 'xenial':
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

pkg_apt = {
    'kubelet': {
        'installed': node.metadata.get('kubernetes', False),
    },
    'kubeadm': {
        'installed': node.metadata.get('kubernetes', False),
    },
    'kubectl': {
        'installed': node.metadata.get('kubernetes', False),
    },
    'kubernetes-cni': {
        'installed': node.metadata.get('kubernetes', False),
    },
}

actions = {}

if node.metadata.get('kubernetes', False):
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
