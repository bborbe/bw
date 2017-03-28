svc_systemd = {}
pkg_apt = {}

pkg_apt['tomcat7'] = {
    'installed': node.metadata.get('tomcat7', {}).get('enabled', False),
}

svc_systemd['tomcat7'] = {
    'running': node.metadata.get('tomcat7', {}).get('enabled', False),
    'enabled': node.metadata.get('tomcat7', {}).get('enabled', False),
    'needs': ['pkg_apt:tomcat7'],
}
