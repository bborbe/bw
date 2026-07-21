# openvpn

OpenVPN server hub (tcp4 :563, subnet 172.16.90.0/24, topology subnet), migrated
1:1 from the legacy `world` tool (`pkg/openvpn`). Adopt-in-place: every deployed
byte reproduces what world already put on the node — `server.conf` and
`/etc/default/openvpn` are verbatim copies of the live files, keys come from the
same laptop PKI world used.

## Layout

- `/etc/openvpn/server.conf` — static copy of the live config (no templating)
- `/etc/openvpn/keys/{ca.crt,server.crt,server.key,dh.pem,ta.key}` — rendered
  from `~/.openvpn/hetzner/` on the operator laptop (world's PKI store; valid
  until 2030). Items are skipped entirely when that directory is absent, so a
  PKI-less machine (CI) can never clobber key material.
- `/etc/openvpn/ccd/<client>` — generated from `node.metadata['openvpn']['clients']`:
  `ifconfig-push <vpn_ip> 255.255.255.0` + `iroute <lan_ip>/32`. No purge —
  legacy unmanaged clients (e.g. nova) keep their ccd files.
- `/etc/openvpn/ip_pool` — NOT managed: `ifconfig-pool-persist` runtime state,
  rewritten by the daemon itself.

## Related node metadata (not in this bundle)

- iptables: `-A INPUT ... --dport 563 -j ACCEPT` + tun0/eth0 FORWARD rules
- sysctl: `net.ipv4.ip_forward = 1`

## PKI / cert lifecycle

The CA (`~/.openvpn/hetzner/ca.key`, laptop-only) signs server + client certs;
everything is valid until 2030 (opnsense 2035). New client certs are signed
out-of-band (~once a year) — see the "Migrate OpenVPN to BundleWrap" task notes.
Renewal gotchas: clients use `remote-cert-tls client`, so a reissued SERVER cert
must carry both ClientAuth and ServerAuth EKUs; certificate serials are not
checked (no CRL).

Securing the PKI storage (encrypted in-repo vault or TeamVault instead of plain
laptop files) is a tracked follow-up task.
