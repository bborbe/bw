def install_git(metadata):
    metadata.setdefault('apt', {}).setdefault('packages', {}).setdefault('git',{})['installed'] = True
    return metadata
