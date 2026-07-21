from os.path import exists, expanduser, join

directories = {}
files = {}
svc_systemd = {}
pkg_apt = {}

openvpn_cfg = node.metadata.get('openvpn', {})

# PKI lives unencrypted in ~/.openvpn/hetzner/ on the operator laptop — exactly
# where the legacy world tool kept and read it (faithful refactoring; securing
# the storage is a tracked follow-up). Key/cert items are only declared when
# the local PKI is present, so an apply from a machine without it can never
# overwrite good key material on the node (it just skips those items).
PKI_DIR = expanduser('~/.openvpn/hetzner')


def local_pki(filename):
    with open(join(PKI_DIR, filename), 'r') as fh:
        return fh.read()


if openvpn_cfg.get('enabled', False):
    pkg_apt['openvpn'] = {
        'installed': True,
    }

    for path in (
        '/etc/openvpn/keys',
        '/etc/openvpn/ccd',
        '/var/log/openvpn',
    ):
        directories[path] = {
            'owner': 'root',
            'group': 'root',
            'mode': '0700',
            # ccd intentionally has no purge: legacy/unmanaged client files
            # (e.g. nova) stay on disk until decommissioned explicitly.
        }

    files['/etc/openvpn/server.conf'] = {
        'source': 'server.conf',
        'content_type': 'text',
        'owner': 'root',
        'group': 'root',
        'mode': '0600',
        'needs': ['pkg_apt:openvpn'],
        'triggers': ['svc_systemd:openvpn@server:restart'],
    }

    files['/etc/default/openvpn'] = {
        'source': 'openvpn.default',
        'content_type': 'text',
        'owner': 'root',
        'group': 'root',
        'mode': '0644',
        'needs': ['pkg_apt:openvpn'],
    }

    # Note: /etc/openvpn/ip_pool is deliberately NOT managed. It is
    # ifconfig-pool-persist runtime state that the openvpn daemon itself
    # rewrites; managing it would show permanent drift.

    for name, client in sorted(openvpn_cfg.get('clients', {}).items()):
        files['/etc/openvpn/ccd/' + name] = {
            'content': (
                'ifconfig-push {} 255.255.255.0\n'
                'iroute {} 255.255.255.255\n'
            ).format(client['vpn_ip'], client['lan_ip']),
            'owner': 'root',
            'group': 'root',
            'mode': '0600',
            'needs': ['directory:/etc/openvpn/ccd'],
            # ccd files are read per client connect — no server restart needed.
        }

    if exists(PKI_DIR):
        for filename, mode in (
            ('ca.crt', '0600'),
            ('server.crt', '0600'),
            ('server.key', '0600'),
            ('dh.pem', '0600'),
            ('ta.key', '0600'),
        ):
            files['/etc/openvpn/keys/' + filename] = {
                'content': local_pki(filename),
                'owner': 'root',
                'group': 'root',
                'mode': mode,
                'needs': ['directory:/etc/openvpn/keys'],
                'triggers': ['svc_systemd:openvpn@server:restart'],
            }

    svc_systemd['openvpn'] = {
        'running': True,
        'enabled': True,
        'needs': ['pkg_apt:openvpn'],
    }
    svc_systemd['openvpn@server'] = {
        'running': True,
        'enabled': True,
        'needs': [
            'pkg_apt:openvpn',
            'file:/etc/openvpn/server.conf',
        ],
    }
