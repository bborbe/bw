if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

files = {}

if len(node.metadata.get('mdadm', {})) > 0:
    files['/etc/mdadm/mdadm.conf'] = {
        'source': 'mdadm.conf',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'context': {
            'data': node.metadata.get('mdadm', {}),
        },
    }
