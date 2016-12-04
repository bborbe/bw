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

svc_systemd = {
    'kubelet': {
        'running': node.metadata.get('kubernetes', False),
        'enabled': node.metadata.get('kubernetes', False),
        'needs': ['pkg_apt:kubelet', 'action:kube_init'],
    },
}

actions = {}

if node.metadata.get('kubernetes', False):
    actions['kube_init'] = {
        'command': 'rm -rf /var/lib/kubelet/* && kubeadm init --use-kubernetes-version {version}'.format(version='v1.4.6'),
        'unless': 'test -e /etc/kubernetes/admin.conf',
        'needs': ['pkg_apt:kubelet', 'pkg_apt:kubeadm'],
    }
