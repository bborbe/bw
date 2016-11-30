def docker_repo(metadata):
    release = metadata.get('release', '')
    metadata.setdefault('apt', {}).setdefault('repos', {})
    metadata['apt']['repos']['docker'] = {
        'gpg_key': '2C52609D',
        'sources': ['deb https://apt.dockerproject.org/repo ubuntu-{} main'.format(release)],
        'installed': metadata.get('docker', False),
    }
    return metadata
