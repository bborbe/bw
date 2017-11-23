@metadata_processor
def defaultnameservers(metadata):
    metadata.setdefault('networking', {}).setdefault('nameservers', ['8.8.4.4', '8.8.8.8'])
    return metadata, DONE


@metadata_processor
def enable_routing(metadata):
    if metadata.get('networking', {}).get('enabled', False):
        options = metadata.setdefault('sysctl', {}).setdefault('options', {})
        options['net.ipv4.ip_forward'] = '1'
    return metadata, DONE
