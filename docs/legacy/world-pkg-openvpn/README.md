# world pkg/openvpn — preserved reference implementation

Source: `github.com/bborbe/world` (repo deleted 2026-07-21 after full migration
to bw), final commit `929ac5a`. Preserved verbatim before deletion.

This is the Go mini-CA + OpenVPN provisioning code that originally built and
managed the VPN now owned by `bundles/openvpn` + `bundles/openvpn-client`:

- `server-config.go` — CA/server cert generation (RSA 4096, PKCS1), dhparam,
  ta.key; the CA private key stayed on the operator laptop (`~/.openvpn/`)
- `client-config.go` — client cert signing + the client.conf template
- `server.go` / `client-remote.go` / `client-local.go` — deployment logic
  (superseded by the bw bundles)
- `openvpn.go` — types (IRoutes/ClientIPs → now node metadata `clients` map)

Kept for the 2030 cert renewal and as the authoritative answer to "how were
these certs generated". Renewal gotchas are documented in
`bundles/openvpn/README.md`. Not compiled, not imported — reference only.
