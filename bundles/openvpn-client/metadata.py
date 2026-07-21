defaults = {
    'openvpn-client': {
        # OpenVPN client (migrated from the legacy world tool). Disabled by
        # default; enable per node and set 'name' to the client's PKI/cert
        # CommonName (usually the short host name, e.g. 'co2hz').
        'enabled': False,
        'name': None,
    },
}
