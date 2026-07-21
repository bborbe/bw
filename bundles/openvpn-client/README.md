# openvpn-client

OpenVPN client for the hetzner VPN hub (tcp4 :563), migrated 1:1 from the
legacy `world` tool (`pkg/openvpn` RemoteClient). Adopt-in-place: every
deployed byte reproduces what world already put on the nodes — `client.conf`
is a verbatim copy of the live file (identical on all clients: static IPs and
iroutes come from the server's ccd, so the client config carries no
per-client values), keys come from the same laptop PKI world used.

## Layout

- `/etc/openvpn/client.conf` — static copy of the live config (no templating;
  Viscosity `#viscosity` comment lines are inert)
- `/etc/openvpn/{ca.crt,client.crt,client.key,ta.key}` — rendered from
  `~/.openvpn/<name>/` on the operator laptop (world's PKI store). Items are
  skipped entirely when that directory is absent, so a PKI-less machine (CI)
  can never clobber key material; a present-but-incomplete PKI fails loudly.
- unit `openvpn@client` (+ the distro's oneshot `openvpn.service` aggregate)

## Node metadata

```python
'openvpn-client': {
    'enabled': True,
    'name': 'co2hz',  # PKI dir + cert CommonName
},
```

The client's static VPN IP and iroute live on the SERVER (bw `openvpn` bundle,
`ccd/<name>`), not here.

## PKI / cert lifecycle

See `bundles/openvpn/README.md` — same CA, same 2030 renewal notes. Securing
the PKI storage is a tracked follow-up task.
