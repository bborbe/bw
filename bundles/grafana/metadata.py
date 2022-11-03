@metadata_reactor
def grafana_repo(metadata):
    if metadata.get('grafana', {}).get('enabled', False):
        return {
            'apt': {
                'repos': {
                    'grafana': {
                        'installed': True,
                        'gpg_key': '4E40DDF6D76E284A4A6780E48C8C34C524098CB6',
                        'sources': ['deb https://packages.grafana.com/oss/deb stable main'],
                    },
                }
            }
        }
    else:
        return {}


@metadata_reactor
def iptables(metadata):
    rules = set()
    if metadata.get('mosquitto', {}).get('enabled', False):
        rules.add('-A INPUT -m state --state NEW -p tcp --dport 3000 -j ACCEPT')
    return {
        'iptables': {
            'rules': {
                'filter': rules,
            },
        },
    }
