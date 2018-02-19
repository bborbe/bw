if node.os != 'ubuntu' and node.os != 'debian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {}
svc_systemd = {}

kvm_packages = (
    'libvirt-bin',
    'virt-top',
    'virtinst',
    'qemu-utils',
    'qemu-kvm',
)

kvm_gui_packages = (
    'virt-manager',
    'spice-client-gtk',
)

for pkg in kvm_packages:
    pkg_apt[pkg] = {
        'installed': node.metadata.get('kvm', {}).get('enabled', False),
    }

for pkg in kvm_gui_packages:
    pkg_apt[pkg] = {
        'installed': node.metadata.get('kvm', {}).get('enabled', False) and node.metadata.get('kvm', {}).get('gui', False),
    }

if node.metadata.get('kvm', {}).get('enabled', False):
    svc_systemd['libvirt-bin'] = {
        'running': True,
        'enabled': True,
        'needs': ['pkg_apt:libvirt-bin'],
    }
else:
    svc_systemd['libvirt-bin'] = {
        'running': False,
        'enabled': False,
    }
