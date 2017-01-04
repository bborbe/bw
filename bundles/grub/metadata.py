def default_cmd_args(metadata):
    metadata.setdefault('grub', {}).setdefault('cmd_args', {}).setdefault('net.ifnames=0', {})
    if metadata.get('grub', {}).get('serial', False):
        metadata.setdefault('grub', {}).setdefault('cmd_args', {}).setdefault('console=tty0', {})
        metadata.setdefault('grub', {}).setdefault('cmd_args', {}).setdefault('console=ttyS0,115200n8', {})
    return metadata
