// Copyright (c) 2019 Benjamin Borbe All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package openvpn

import (
	"context"

	"github.com/bborbe/errors"

	"github.com/bborbe/world/pkg/network"
	"github.com/bborbe/world/pkg/validation"
)

type Device string

func (d Device) Validate(ctx context.Context) error {
	if d == "" {
		return errors.New(ctx, "Device empty")
	}
	return nil
}

func (d Device) String() string {
	return string(d)
}

const Tap Device = "tap"

const Tun Device = "tun"

type ClientName string

func (c ClientName) String() string {
	return string(c)
}

func (c ClientName) Validate(ctx context.Context) error {
	if c == "" {
		return errors.New(ctx, "ClientName empty")
	}
	return nil
}

type ServerName string

func (s ServerName) String() string {
	return string(s)
}

func (s ServerName) Validate(ctx context.Context) error {
	if s == "" {
		return errors.New(ctx, "ServerName empty")
	}
	return nil
}

type ServerAddress string

func (s ServerAddress) String() string {
	return string(s)
}

func (s ServerAddress) Validate(ctx context.Context) error {
	if s == "" {
		return errors.New(ctx, "ServerName empty")
	}
	return nil
}

type IRoute struct {
	Name  ClientName
	IPNet network.IPNet
}

func (r IRoutes) Validate(ctx context.Context) error {
	for _, route := range r {
		if err := route.Validate(ctx); err != nil {
			return err
		}
	}
	return nil
}

type IRoutes []IRoute

func (r IRoute) Validate(ctx context.Context) error {
	return validation.Validate(
		ctx,
		r.IPNet,
		r.Name,
	)
}

type Routes []Route

func (r Routes) Validate(ctx context.Context) error {
	for _, route := range r {
		if err := route.Validate(ctx); err != nil {
			return err
		}
	}
	return nil
}

type Route struct {
	Gateway network.IP
	IPNet   network.IPNet
}

func (r Route) Validate(ctx context.Context) error {
	return validation.Validate(
		ctx,
		r.IPNet,
		r.Gateway,
	)
}

type ClientIPs []ClientIP

func (c ClientIPs) Validate(ctx context.Context) error {
	for _, clientIP := range c {
		if err := clientIP.Validate(ctx); err != nil {
			return err
		}
	}
	return nil
}

type ClientIP struct {
	Name ClientName
	IP   network.IP
}

func (c ClientIP) Validate(ctx context.Context) error {
	return validation.Validate(
		ctx,
		c.Name,
		c.IP,
	)
}
