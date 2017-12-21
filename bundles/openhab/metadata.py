@metadata_processor
def user(metadata):
    metadata.setdefault('users', {}).setdefault('openhab', {})['enabled'] = metadata.get('openhab', {}).get('enabled', False)
    return metadata, DONE


@metadata_processor
def iptables(metadata):
    if metadata.get('openhab', {}).get('enabled', False):
        rules = [
            # openHAB ports
            '-A INPUT -m state --state NEW -p tcp --dport 8080 -j ACCEPT',
            '-A INPUT -m state --state NEW -p tcp --dport 8443 -j ACCEPT',
        ]
        list = metadata.setdefault('iptables', {}).setdefault('rules', {}).setdefault('filter', [])
        for i in rules:
            if i not in list:
                list.append(i)
    return metadata, DONE


@metadata_processor
def install_apt_packages(metadata):
    for package_name in ['curl', 'unzip', 'openjdk-8-jdk']:
        metadata.setdefault('apt', {}).setdefault('packages', {}).setdefault(package_name, {})
        metadata['apt']['packages'][package_name]['installed'] = \
            metadata['apt']['packages'][package_name].get('installed', False) or metadata.get('openhab', {}).get('enabled', False)
    return metadata, DONE
