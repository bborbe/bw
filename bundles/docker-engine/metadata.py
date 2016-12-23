def docker_repo(metadata):
    if metadata.get('docker', {}).get('enabled', False):
        release = metadata.get('release', '')
        metadata.setdefault('apt', {}).setdefault('repos', {})
        metadata['apt']['repos']['docker'] = {
            'gpg_key': '2C52609D',
            'sources': ['deb https://apt.dockerproject.org/repo ubuntu-{} main'.format(release)],
            'installed': metadata.get('docker', False),
        }
    return metadata


def docker_cleanup_cron(metadata):
    if metadata.get('docker', {}).get('enabled', False):
        metadata.setdefault('cron', {}).setdefault('jobs', {})
        metadata['cron']['jobs']['docker-cleanup-container'] = '15 * * * * root docker ps -a -q -f status=exited | xargs --no-run-if-empty docker rm -v'
        metadata['cron']['jobs']['docker-cleanup-images'] = '30 * * * * root docker images -f "dangling=true" -q | xargs --no-run-if-empty docker rmi'
    return metadata
