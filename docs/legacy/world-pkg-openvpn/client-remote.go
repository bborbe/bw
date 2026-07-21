// Copyright (c) 2019 Benjamin Borbe All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package openvpn

import (
	"context"

	"github.com/bborbe/world/configuration/service"
	"github.com/bborbe/world/pkg/apt"
	"github.com/bborbe/world/pkg/file"
	"github.com/bborbe/world/pkg/network"
	"github.com/bborbe/world/pkg/remote"
	"github.com/bborbe/world/pkg/ssh"
	"github.com/bborbe/world/pkg/validation"
	"github.com/bborbe/world/pkg/world"
)

type RemoteClient struct {
	SSH           *ssh.SSH
	ClientName    ClientName
	ServerName    ServerName
	ServerAddress ServerAddress
	ServerPort    network.Port
	Routes        Routes
	Device        Device
}

func (r *RemoteClient) Validate(ctx context.Context) error {
	return validation.Validate(
		ctx,
		r.SSH,
		r.ClientName,
		r.ServerName,
		r.ServerAddress,
		r.ServerPort,
		r.clientConfig(),
		r.Device,
	)
}

func (r *RemoteClient) Children(ctx context.Context) (world.Configurations, error) { //nolint:funlen
	clientConfig := r.clientConfig()
	return world.Configurations{
		&service.Directory{
			SSH:   r.SSH,
			Path:  file.Path("/etc/openvpn"),
			User:  "root",
			Group: "root",
			Perm:  0700,
		},
		&remote.File{
			SSH: r.SSH,
			Path: file.PathFunc(func(ctx context.Context) (string, error) {
				return "/etc/openvpn/client.conf", nil
			}),
			User:    "root",
			Group:   "root",
			Perm:    0600,
			Content: clientConfig.ConfigContent(),
		},
		&remote.FileLocalCached{
			SSH:       r.SSH,
			Path:      file.Path("/etc/openvpn/ca.crt"),
			LocalPath: clientConfig.LocalPathCaCrt(),
			User:      "root",
			Group:     "root",
			Perm:      0600,
			Content:   clientConfig.CaCrt(),
		},
		&remote.FileLocalCached{
			SSH:       r.SSH,
			Path:      file.Path("/etc/openvpn/ta.key"),
			LocalPath: clientConfig.LocalPathTaKey(),
			User:      "root",
			Group:     "root",
			Perm:      0600,
			Content:   clientConfig.TAKey(),
		},
		&remote.FileLocalCached{
			SSH:       r.SSH,
			Path:      file.Path("/etc/openvpn/client.key"),
			LocalPath: clientConfig.LocalPathClientKey(),
			User:      "root",
			Group:     "root",
			Perm:      0600,
			Content:   clientConfig.ClientKey(),
		},
		&remote.FileLocalCached{
			SSH:       r.SSH,
			Path:      file.Path("/etc/openvpn/client.crt"),
			LocalPath: clientConfig.LocalPathClientCrt(),
			User:      "root",
			Group:     "root",
			Perm:      0600,
			Content:   clientConfig.ClientCrt(),
		},
		world.NewConfiguraionBuilder().WithApplier(&apt.Update{
			SSH: r.SSH,
		}),
		world.NewConfiguraionBuilder().WithApplier(&apt.Install{
			SSH:     r.SSH,
			Package: "openvpn",
		}),
		world.NewConfiguraionBuilder().WithApplier(&apt.Autoremove{
			SSH: r.SSH,
		}),
		world.NewConfiguraionBuilder().WithApplier(&apt.Clean{
			SSH: r.SSH,
		}),
		&remote.File{
			SSH:     r.SSH,
			Path:    file.Path("/etc/default/openvpn"),
			User:    "root",
			Group:   "root",
			Perm:    0644,
			Content: clientConfig.ServerConfig.OpenvpnDefaultConf(),
		},
		world.NewConfiguraionBuilder().WithApplier(&remote.ServiceStart{
			SSH:  r.SSH,
			Name: "openvpn",
		}),
		world.NewConfiguraionBuilder().WithApplier(&remote.ServiceStart{
			SSH:  r.SSH,
			Name: "openvpn@client",
		}),
	}, nil
}

func (r *RemoteClient) Applier() (world.Applier, error) {
	return nil, nil
}

func (r *RemoteClient) clientConfig() ClientConfig {
	return ClientConfig{
		ClientName:    r.ClientName,
		ServerAddress: r.ServerAddress,
		ServerConfig: ServerConfig{
			ServerName: r.ServerName,
			ServerPort: r.ServerPort,
		},
		Routes: r.Routes,
		Device: r.Device,
	}
}
