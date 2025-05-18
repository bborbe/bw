if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

files = {}

if len(node.metadata.get('udev', {})) > 0:
    files['/etc/udev/rules.d/10-network.rules'] = {
        'source': '10-network.rules',
        'content_type': 'mako',
        'context': {
            'modules': node.metadata.get('udev', {}),
        },
        'owner': 'root',
        'group': 'root',
        'mode': '0644',
    }
else:
    files['/etc/udev/rules.d/10-network.rules'] = {
        'delete': True,
    }
