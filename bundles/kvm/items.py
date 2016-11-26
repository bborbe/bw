os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if os != 'ubuntu' or release != 'xenial':
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

pkg_apt = {
    'virt-top': {
        'installed': node.metadata.get('kvm', False),
    },
    'virtinst': {
        'installed': node.metadata.get('kvm', False),
    },
}
