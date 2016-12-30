def default_cmd_args(metadata):
    metadata.setdefault('grub', {}).setdefault('cmd_args', {}).setdefault('net.ifnames=0', {})
    return metadata
