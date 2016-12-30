nodes['hm.nuke'] = {
    'hostname': 'nuke.hm.benjamin-borbe.de',
    'metadata': {
        'os': 'debian',
        'release': 'jessie',
        'networking': {
            'enabled': True,
            'interfaces': {
                'eth0': {
                    'address': '192.168.178.5',
                    'netmask': '255.255.255.0',
                    'gateway': '192.168.178.1',
                    'dns-nameservers': '8.8.4.4 8.8.8.8',
                },
            },
        },
        'grub': {
            'enabled': True,
            'default': '"Windows 10 (loader) (on /dev/sdi1)"',
            'cmd_args': {
                'intel_iommu=on': {},
                'vfio-pci.ids=10de:13c2,10de:0fbb,1b4b:9230': {},
            },
        },
        'kvm': {
            'enabled': True,
        },
        'iptables': {
            'enabled': True,
            'nat_interfaces': [],
            'rules': {
                'filter': [
                    # allow forward
                    '-A FORWARD -j ACCEPT',
                ],
            },
        },
        'kernel_modules': {
            'vfio': {},
            'vfio_iommu_type1': {},
            'vfio_pci': {},
            'vfio_virqfd': {},
        },
    },
}
