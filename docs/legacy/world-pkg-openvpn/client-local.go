// Copyright (c) 2019 Benjamin Borbe All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package openvpn

import (
	"context"

	"github.com/bborbe/world/pkg/local"
	"github.com/bborbe/world/pkg/network"
	"github.com/bborbe/world/pkg/validation"
	"github.com/bborbe/world/pkg/world"
)

type LocalClient struct {
	ClientName    ClientName
	ServerName    ServerName
	ServerAddress ServerAddress
	Routes        Routes
	ServerPort    network.Port
	Device        Device
}

func (l *LocalClient) Validate(ctx context.Context) error {
	return validation.Validate(
		ctx,
		l.ClientName,
		l.ServerName,
		l.ServerAddress,
		l.ServerPort,
		l.clientConfig(),
		l.Device,
	)
}

func (l *LocalClient) Children(ctx context.Context) (world.Configurations, error) {
	clientConfig := l.clientConfig()
	return world.Configurations{
		world.NewConfiguraionBuilder().WithApplier(
			&local.FileContent{
				Path:    clientConfig.LocalPathConfig(),
				Content: clientConfig.ConfigContent(),
			},
		),
		world.NewConfiguraionBuilder().WithApplier(
			&local.FileContent{
				Path:    clientConfig.LocalPathCaCrt(),
				Content: clientConfig.CaCrt(),
			},
		),
		world.NewConfiguraionBuilder().WithApplier(
			&local.FileContent{
				Path:    clientConfig.LocalPathTaKey(),
				Content: clientConfig.TAKey(),
			},
		),
		world.NewConfiguraionBuilder().WithApplier(
			&local.FileContent{
				Path:    clientConfig.LocalPathClientKey(),
				Content: clientConfig.ClientKey(),
			},
		),
		world.NewConfiguraionBuilder().WithApplier(
			&local.FileContent{
				Path:    clientConfig.LocalPathClientCrt(),
				Content: clientConfig.ClientCrt(),
			},
		),
	}, nil
}

func (l *LocalClient) Applier() (world.Applier, error) {
	return nil, nil
}

func (l *LocalClient) clientConfig() ClientConfig {
	return ClientConfig{
		ClientName:    l.ClientName,
		ServerAddress: l.ServerAddress,
		ServerConfig: ServerConfig{
			ServerName: l.ServerName,
			ServerPort: l.ServerPort,
		},
		Routes: l.Routes,
		Device: l.Device,
	}
}
