if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

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
    'spice-client-gtk': {
        'installed': node.metadata.get('kvm', {}).get('enabled', False) and node.metadata.get('kvm', {}).get('gui', False),
    },
}
