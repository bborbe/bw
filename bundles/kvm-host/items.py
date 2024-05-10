if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

files = {}
pkg_apt = {}
svc_systemd = {}
directories = {}
symlinks = {}

if node.metadata.get('kvm', {}).get('enabled', False):
    svc_systemd['libvirtd'] = {
        'running': True,
        'enabled': True,
    }
    files['/etc/sysctl.d/70-bridge.conf'] = {
        'source': 'bridge.conf',
        'content_type': 'text',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
    }
    files['/etc/udev/rules.d/99-bridge.rules'] = {
        'content': 'ACTION=="add", SUBSYSTEM=="module", KERNEL=="br_netfilter", RUN+="/sbin/sysctl -p /etc/sysctl.d/70-bridge.conf"',
        'mode': "0644",
    }
    files['/etc/libvirt/qemu/networks/br0.xml'] = {
        'source': 'br0.xml',
        'content_type': 'text',
        'mode': '0600',
        'owner': 'root',
        'group': 'root',
    }
    symlinks['/etc/libvirt/qemu/networks/autostart/br0.xml'] = {
        'group': 'root',
        'owner': 'root',
        'target': '/etc/libvirt/qemu/networks/br0.xml',
    }
