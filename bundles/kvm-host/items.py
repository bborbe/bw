if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

files = {}
pkg_apt = {}
svc_systemd = {}
directories = {}
symlinks = {}
actions = {}

if node.metadata.get('kvm-host', {}).get('enabled', False):
    svc_systemd['libvirtd'] = {
        'running': True,
        'enabled': True,
    }
    files['/etc/libvirt/qemu.conf'] = {
        'source': 'qemu.conf',
        'content_type': 'text',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'triggers': ['svc_systemd:libvirtd:restart'],
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

    # nwfilter support for VM network restrictions
    directories['/etc/bundlewrap/nwfilter'] = {
        'owner': 'root',
        'group': 'root',
        'mode': '0755',
    }

    for vm_name, filter_config in node.metadata.get('kvm-host', {}).get('nwfilters', {}).items():
        filter_name = f'restrict-{vm_name}'

        # Store our template in bundlewrap directory (not libvirt's)
        files[f'/etc/bundlewrap/nwfilter/{filter_name}.xml'] = {
            'source': 'nwfilter.xml',
            'content_type': 'mako',
            'mode': '0644',
            'owner': 'root',
            'group': 'root',
            'context': {
                'filter_name': filter_name,
                'rules': filter_config.get('rules', []),
            },
            'triggers': [f'action:nwfilter_reload_{filter_name}'],
        }

        # Only define if different from current
        actions[f'nwfilter_reload_{filter_name}'] = {
            'command': f'virsh nwfilter-define /etc/bundlewrap/nwfilter/{filter_name}.xml',
            'triggered': True,
        }
