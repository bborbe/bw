@metadata_reactor.provides(
    'grub/cmd_default_args',
    'grub/cmd_args',
)
def default_cmd_args(metadata):
    result = {
        'grub': {
            'cmd_args': {},
            'cmd_default_args': {
                'quiet': {},
            },
        }
    }
    if not metadata.get('grub', {}).get('predictable-nic', False):
        result['grub']['cmd_args']['net.ifnames=0'] = {}
    if metadata.get('grub', {}).get('serial', False):
        result['grub']['cmd_args']['console=tty0'] = {}
        result['grub']['cmd_args']['console=ttyS0,115200n8'] = {}
    return result
