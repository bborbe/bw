@metadata_processor
def user(metadata):
    metadata.setdefault('users', {}).setdefault('openhab', {})['enabled'] = metadata.get('openhab', {}).get('enabled', False)
    return metadata, DONE


@metadata_processor
def openhab_repo(metadata):
    metadata.setdefault('apt', {}).setdefault('repos', {})
    metadata['apt']['repos']['openhab'] = {
        'gpg_key': 'A224060A',
        'sources': ['deb https://dl.bintray.com/openhab/apt-repo2 stable main'],
        'installed': metadata.get('openhab', {}).get('enabled', False),
    }
    return metadata, DONE

