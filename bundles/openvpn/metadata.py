defaults = {
    'openvpn': {
        # OpenVPN server hub (migrated from the legacy world tool). Disabled by
        # default; enable per node and provide the ccd client map.
        'enabled': False,
        # name -> {'vpn_ip': ..., 'lan_ip': ...}; renders one ccd file per
        # client: ifconfig-push <vpn_ip> (static tunnel IP, topology subnet)
        # + iroute <lan_ip>/32 (routes the client's LAN address into the tun).
        'clients': {},
    },
}
