svc_systemd = {}
pkg_apt = {}

if node.metadata.get('tomcat7', {}).get('enabled', False):
    pkg_apt['tomcat7'] = {
        'installed': True,
    }
    svc_systemd['tomcat7'] = {
        'running': True,
        'enabled': True,
        'needs': ['pkg_apt:tomcat7'],
    }
else:
    pkg_apt['tomcat7'] = {
        'installed': False,
    }
    svc_systemd['tomcat7'] = {
        'running': False,
        'enabled': False,
    }
