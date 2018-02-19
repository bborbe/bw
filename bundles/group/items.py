if node.os != 'ubuntu' and node.os != 'debian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

groups = {}

for groupname, data in node.metadata.get('groups', {}).items():
    if 'enabled' in data:
        group = {}
        if data.get('enabled', False):
            for field in ['gid']:
                if field in data:
                    group[field] = data[field]
        else:
            group['delete'] = True
        groups[groupname] = group
