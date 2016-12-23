groups['all'] = {
    'member_patterns': (
        r'.*',
    ),
    'bundles': (
        'git',
        'user',
        'authorized_key',
        'dotfiles',
    ),
    'metadata': {
        'users': {
            'bborbe': {
                'sudo': True,
                'authorized_keys': {
                    'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCOw/yh7+j3ygZp2aZRdZDWUh0Dkj5N9/USdiLSoS+0CHJta+mtSxxmI/yv1nOk7xnuA6qtjpxdMlWn5obtC9xyS6T++tlTK9gaPwU7a/PObtoZdfQ7znAJDpX0IPI06/OH1tFE9kEutHQPzhCwRaIQ402BHIrUMWzzP7Ige8Oa0HwXH4sHUG5h/V/svzi9T0CKJjF8dTx4iUfKX959hT8wQnKYPULewkNBFv6pNfWIr8EzvIEQcPmmm3tP+dQPKg5QKVi6jPdRla+t5HXfhXu0W3WCDa2s0VGmJjBdMMowr5MLNYI79MKziSV1w1IWL17Z58Lop0zEHqP7Ba0Aooqd': {},
                },
                'full_name': 'Benjamin Borbe',
                'dotfiles': 'https://github.com/bborbe/dotfiles.git',
            },
            'root': {
                'home': '/root',
            },
            'pi': {
                'deleted': True,
            },
        },
    },
}
