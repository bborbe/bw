os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

pkg_apt = {
    'qemu-kvm': {
        'installed': node.metadata.get('kvm', {}).get('enabled', False),
    },
    'virt-top': {
        'installed': node.metadata.get('kvm', {}).get('enabled', False),
    },
    'virtinst': {
        'installed': node.metadata.get('kvm', {}).get('enabled', False),
    },
    'virt-manager': {
        'installed': node.metadata.get('kvm', {}).get('enabled', False) and node.metadata.get('kvm', {}).get('gui', False),
    },
    'libvirt-daemon-system': {
        'installed': node.metadata.get('kvm', {}).get('enabled', False) and node.metadata.get('kvm', {}).get('gui', False),
    },
    'spice-client-gtk': {
        'installed': node.metadata.get('kvm', {}).get('enabled', False) and node.metadata.get('kvm', {}).get('gui', False),
    },
}
