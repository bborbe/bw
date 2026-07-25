groups['k3s'] = {
    'member_patterns': (
        r'.*k3s.*',
    ),
    'metadata': {
        # Raise the ARP/neighbour table limits well above the kernel defaults
        # (128/512/1024). k3s nodes run one veth per pod, and `arp_tbl` is a
        # single GLOBAL kernel table counting entries across every network
        # namespace -- so the host-visible `ip neigh show` count badly
        # understates the real total.
        #
        # 2026-07-25, nuke-k3s-prod-0: 389 veth interfaces, `ip neigh show`
        # reported only 404 entries (apparently well under the 1024 default),
        # yet the kernel logged "neighbour: arp_cache: neighbor table
        # overflow!" ~7000x/hour continuously. Once the table is full
        # neigh_alloc() fails and any packet needing a NEW neighbour entry is
        # silently dropped, which produced ~35% DNS failures and recurring
        # ImagePullBackOff. systemd-resolved itself logged zero timeouts --
        # the queries never made it off the box.
        'sysctl': {
            'options': {
                'net.ipv4.neigh.default.gc_thresh1': '4096',
                'net.ipv4.neigh.default.gc_thresh2': '8192',
                'net.ipv4.neigh.default.gc_thresh3': '16384',
            },
        },
    },
}
