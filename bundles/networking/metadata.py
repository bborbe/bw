def defaultnameservers(metadata):
    metadata.setdefault('networking', {}).setdefault('nameservers', ['8.8.4.4', '8.8.8.8'])
    return metadata
