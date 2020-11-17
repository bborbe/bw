@metadata_reactor
def default_cmd_args(metadata):
    result = {
        'grub': {
            'cmd_args': {
                'net.ifnames=0': {},
                'acpi=noirq': {},
            }
        }
    }
    if metadata.get('grub', {}).get('serial', False):
        result['grub']['cmd_args']['console=tty0'] = {}
        result['grub']['cmd_args']['console=ttyS0,115200n8'] = {}
    return result
