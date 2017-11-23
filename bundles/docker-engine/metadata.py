@metadata_processor
def docker_repo(metadata):
    if metadata.get('docker', {}).get('enabled', False):
        release = metadata.get('release', '')
        metadata.setdefault('apt', {}).setdefault('repos', {})
        metadata['apt']['repos']['docker'] = {
            'gpg_key': '2C52609D',
            'sources': ['deb https://apt.dockerproject.org/repo {os}-{release} main'.format(os=metadata.get('os'), release=release)],
            'installed': metadata.get('docker', False),
        }
    return metadata, DONE


@metadata_processor
def docker_cleanup_cron(metadata):
    metadata.setdefault('cron', {}).setdefault('jobs', {})
    metadata['cron']['jobs']['docker-cleanup-container'] = {
        'enabled': metadata.get('docker', {}).get('enabled', False),
        'schedule': '15 * * * *',
        'expression': 'docker ps -a -q -f status=exited | xargs --no-run-if-empty docker rm -v',
    }
    metadata['cron']['jobs']['docker-cleanup-images'] = {
        'enabled': metadata.get('docker', {}).get('enabled', False),
        'schedule': '30 * * * *',
        'expression': 'docker images -f "dangling=true" -q | xargs --no-run-if-empty docker rmi',
    }
    return metadata, DONE
