// Copyright (c) 2018 Benjamin Borbe All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package openvpn

import (
	"bytes"
	"context"
	"fmt"
	"net"
	"sort"

	"github.com/bborbe/world/configuration/service"
	"github.com/bborbe/world/pkg/apt"
	"github.com/bborbe/world/pkg/content"
	"github.com/bborbe/world/pkg/file"
	"github.com/bborbe/world/pkg/local"
	"github.com/bborbe/world/pkg/network"
	"github.com/bborbe/world/pkg/remote"
	"github.com/bborbe/world/pkg/ssh"
	"github.com/bborbe/world/pkg/validation"
	"github.com/bborbe/world/pkg/world"
)

type Server struct {
	SSH         *ssh.SSH
	ServerName  ServerName
	ServerPort  network.Port
	ServerIPNet network.IPNet
	Routes      Routes
	IRoutes     IRoutes
	ClientIPs   ClientIPs
	Device      Device
}

func (s *Server) Validate(ctx context.Context) error {
	return validation.Validate(
		ctx,
		s.SSH,
		s.ServerName,
		s.ServerIPNet,
		s.ServerPort,
		s.Routes,
		s.IRoutes,
		s.ClientIPs,
		s.Device,
	)
}

func (s *Server) Children(ctx context.Context) (world.Configurations, error) { //nolint:funlen
	serverConfig := s.serverConfig()

	configurations := make([]world.Configuration, 0, 20+len(s.IRoutes))
	configurations = append(configurations, []world.Configuration{
		&service.Directory{
			SSH:   s.SSH,
			Path:  file.Path("/etc/openvpn/keys"),
			User:  "root",
			Group: "root",
			Perm:  0700,
		},
		&service.Directory{
			SSH:   s.SSH,
			Path:  file.Path("/etc/openvpn/ccd"),
			User:  "root",
			Group: "root",
			Perm:  0700,
		},
		&service.Directory{
			SSH:   s.SSH,
			Path:  file.Path("/var/log/openvpn"),
			User:  "root",
			Group: "root",
			Perm:  0700,
		},
		&remote.File{
			SSH:     s.SSH,
			Path:    file.Path("/etc/openvpn/server.conf"),
			User:    "root",
			Group:   "root",
			Perm:    0600,
			Content: serverConfig.ServerConfigContent(),
		},
		&remote.File{
			SSH:     s.SSH,
			Path:    file.Path("/etc/openvpn/ip_pool"),
			User:    "root",
			Group:   "root",
			Perm:    0600,
			Content: s.ipPoolContent(),
		},
		&remote.FileLocalCached{
			SSH:       s.SSH,
			Path:      file.Path("/etc/openvpn/keys/ta.key"),
			LocalPath: serverConfig.LocalPathTaKey(),
			User:      "root",
			Group:     "root",
			Perm:      0600,
			Content:   serverConfig.TAKey(),
		},
		&remote.FileLocalCached{
			SSH:       s.SSH,
			Path:      file.Path("/etc/openvpn/keys/dh.pem"),
			LocalPath: serverConfig.LocalPathDhPem(),
			User:      "root",
			Group:     "root",
			Perm:      0600,
			Content:   serverConfig.DHPem(),
		},
		world.NewConfiguraionBuilder().WithApplier(
			&local.FileContent{
				Path:    serverConfig.LocalPathCAPrivateKey(),
				Content: serverConfig.CAPrivateKey(),
			},
		),
		&remote.FileLocalCached{
			SSH:       s.SSH,
			Path:      file.Path("/etc/openvpn/keys/ca.crt"),
			LocalPath: serverConfig.LocalPathCaCrt(),
			User:      "root",
			Group:     "root",
			Perm:      0600,
			Content:   serverConfig.CaCrt(),
		},
		&remote.FileLocalCached{
			SSH:       s.SSH,
			Path:      file.Path("/etc/openvpn/keys/server.key"),
			LocalPath: serverConfig.LocalPathServerKey(),
			User:      "root",
			Group:     "root",
			Perm:      0600,
			Content:   serverConfig.ServerKey(),
		},
		&remote.FileLocalCached{
			SSH:       s.SSH,
			Path:      file.Path("/etc/openvpn/keys/server.crt"),
			LocalPath: serverConfig.LocalPathServerCrt(),
			User:      "root",
			Group:     "root",
			Perm:      0600,
			Content:   serverConfig.ServerCrt(),
		},
		world.NewConfiguraionBuilder().WithApplier(&remote.IptablesAllowInput{
			SSH:      s.SSH,
			Port:     network.PortStatic(563),
			Protocol: network.TCP,
		}),
		world.NewConfiguraionBuilder().WithApplier(&apt.Update{
			SSH: s.SSH,
		}),
		world.NewConfiguraionBuilder().WithApplier(&apt.Install{
			SSH:     s.SSH,
			Package: "openvpn",
		}),
		world.NewConfiguraionBuilder().WithApplier(&apt.Autoremove{
			SSH: s.SSH,
		}),
		world.NewConfiguraionBuilder().WithApplier(&apt.Clean{
			SSH: s.SSH,
		}),
		&remote.File{
			SSH:     s.SSH,
			Path:    file.Path("/etc/default/openvpn"),
			User:    "root",
			Group:   "root",
			Perm:    0644,
			Content: serverConfig.OpenvpnDefaultConf(),
		},
		world.NewConfiguraionBuilder().WithApplier(&remote.ServiceStart{
			SSH:  s.SSH,
			Name: "openvpn",
		}),
		world.NewConfiguraionBuilder().WithApplier(&remote.ServiceStart{
			SSH:  s.SSH,
			Name: "openvpn@server",
		}),
		&service.Sysctl{
			SSH: s.SSH,
			Options: service.SysctlOptions{
				{
					Option: "net.ipv4.ip_forward",
					Value:  "1",
				},
			},
		},
		world.NewConfiguraionBuilder().WithApplier(&remote.IptablesAllowInput{
			SSH:      s.SSH,
			Port:     serverConfig.ServerPort,
			Protocol: network.TCP,
		}),
		world.NewConfiguraionBuilder().WithApplier(&remote.IptablesAllowForward{
			SSH: s.SSH,
		}),
	}...)

	// Per-client ccd file: authoritative static tunnel IP (ifconfig-push) plus
	// the client's iroute. ifconfig-push is required for a stable VpnIP —
	// ifconfig-pool-persist alone is only advisory, so newly-added clients would
	// otherwise land on a dynamic pool IP instead of their configured VpnIP.
	// topology is "subnet", so the push uses the VPN subnet netmask.
	irouteByName := make(map[ClientName]network.IPNet, len(s.IRoutes))
	for _, iroute := range s.IRoutes {
		irouteByName[iroute.Name] = iroute.IPNet
	}
	serverIPNet := s.ServerIPNet
	for _, clientIP := range s.ClientIPs {
		// iroute is optional: a client with no matching IRoutes entry still gets
		// its ifconfig-push (static IP), just no pushed subnet route. Callers build
		// ClientIPs and IRoutes from the same server slice (see BuildClientIPs /
		// BuildIRoutes), so in practice every ClientIP has a matching IRoute.
		iroute := irouteByName[clientIP.Name]
		configurations = append(configurations, &remote.File{
			SSH:  s.SSH,
			Path: file.Path("/etc/openvpn/ccd/" + clientIP.Name.String()),
			Content: content.Func(func(ctx context.Context) ([]byte, error) {
				vpnIP, err := clientIP.IP.IP(ctx)
				if err != nil {
					return nil, err
				}
				serverNet, err := serverIPNet.IPNet(ctx)
				if err != nil {
					return nil, err
				}
				buf := &bytes.Buffer{}
				fmt.Fprintf(
					buf,
					"ifconfig-push %s %s\n",
					vpnIP.String(),
					net.IP(serverNet.Mask).String(),
				)
				if iroute != nil {
					ipNet, err := iroute.IPNet(ctx)
					if err != nil {
						return nil, err
					}
					fmt.Fprintf(
						buf,
						"iroute %s %s\n",
						ipNet.IP.String(),
						net.IP(ipNet.Mask).String(),
					)
				}
				return buf.Bytes(), nil
			}),
			User:  "root",
			Group: "root",
			Perm:  0600,
		})
	}
	return configurations, nil
}

func (s *Server) serverConfig() ServerConfig {
	return ServerConfig{
		ServerName:  s.ServerName,
		ServerIPNet: s.ServerIPNet,
		ServerPort:  network.PortStatic(563),
		Routes:      s.Routes,
		Device:      s.Device,
	}
}

func (s *Server) Applier() (world.Applier, error) {
	return nil, nil
}

type ipPool []ipPoolEntry

func (i ipPool) Len() int { return len(i) }

func (i ipPool) Less(a, b int) bool {
	c := bytes.Compare(i[a].ip, i[b].ip)
	if c < 0 {
		return true
	}
	if c > 0 {
		return false
	}
	return i[a].name < i[b].name
}

func (i ipPool) Swap(a, b int) { i[a], i[b] = i[b], i[a] }

func (i *ipPool) Bytes() []byte {
	if i == nil {
		return nil
	}
	buf := &bytes.Buffer{}
	for _, e := range *i {
		buf.Write(e.Bytes())
	}
	return buf.Bytes()
}

type ipPoolEntry struct {
	name string
	ip   net.IP
}

func (e ipPoolEntry) Bytes() []byte {
	buf := &bytes.Buffer{}
	fmt.Fprint(buf, e.name)
	fmt.Fprint(buf, ",")
	fmt.Fprintln(buf, e.ip.String())
	return buf.Bytes()
}

func (s *Server) ipPoolContent() content.HasContent {
	return content.Func(func(ctx context.Context) ([]byte, error) {
		var result ipPool
		for _, clientIP := range s.ClientIPs {
			ip, err := clientIP.IP.IP(ctx)
			if err != nil {
				return nil, err
			}
			result = append(result, ipPoolEntry{
				name: clientIP.Name.String(),
				ip:   ip,
			})
		}
		sort.Sort(result)
		return result.Bytes(), nil
	})
}
