def docker_repo(metadata):
    release = metadata.get('release', '')
    metadata.setdefault('apt', {}).setdefault('repos', {})
    metadata['apt']['repos']['kubernetes'] = {
        'gpg_key': 'A7317B0F',
        'sources': ['deb http://apt.kubernetes.io/ kubernetes-{} main'.format(release)],
        'installed': metadata.get('kubernetes', False),
    }
    return metadata
