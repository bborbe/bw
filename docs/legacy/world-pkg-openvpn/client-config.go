// Copyright (c) 2019 Benjamin Borbe All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package openvpn

import (
	"context"
	"crypto/rand"
	"crypto/rsa"
	"crypto/x509"
	"crypto/x509/pkix"
	"encoding/pem"
	"fmt"
	"math/big"
	"net"
	"os"
	"os/user"
	"path"
	"path/filepath"
	"time"

	"github.com/bborbe/world/pkg/content"
	"github.com/bborbe/world/pkg/file"
	"github.com/bborbe/world/pkg/template"
	"github.com/bborbe/world/pkg/validation"
)

type ClientConfig struct {
	ClientName    ClientName
	ServerConfig  ServerConfig
	ServerAddress ServerAddress
	Routes        Routes
	Device        Device
}

func (c ClientConfig) Validate(ctx context.Context) error {
	return validation.Validate(
		ctx,
		c.ServerConfig.ServerName,
		c.ServerConfig.ServerPort,
		c.ClientName,
		c.ServerAddress,
		c.Device,
	)
}

func (c *ClientConfig) ConfigContent() content.HasContent {
	return content.Func(func(ctx context.Context) ([]byte, error) {
		port, err := c.ServerConfig.ServerPort.Port(ctx)
		if err != nil {
			return nil, err
		}

		type Route struct {
			Gateway string
			Net     string
			Mask    string
		}
		data := struct {
			ServerName string
			ServerHost string
			ServerPort int
			Routes     []Route
			Device     string
		}{
			ServerName: c.ServerConfig.ServerName.String(),
			ServerHost: c.ServerAddress.String(),
			ServerPort: port,
			Routes:     []Route{},
			Device:     c.Device.String(),
		}
		for _, route := range c.Routes {
			gateway, err := route.Gateway.IP(ctx)
			if err != nil {
				return nil, err
			}
			ipnet, err := route.IPNet.IPNet(ctx)
			if err != nil {
				return nil, err
			}
			data.Routes = append(data.Routes, Route{
				Gateway: gateway.String(),
				Net:     ipnet.IP.String(),
				Mask:    net.IP(ipnet.Mask).String(),
			})
		}
		return template.Render(`
#viscosity startonopen true
#viscosity usepeerdns false
#viscosity ipv6 false
#viscosity dns off
#viscosity protocol openvpn
#viscosity autoreconnect true
#viscosity dnssupport true
#viscosity name {{.ServerName}}
#viscosity dhcp false

client
dev {{.Device}}
proto tcp4
remote {{.ServerHost}} {{.ServerPort}}
resolv-retry infinite
nobind
persist-key
persist-tun
ca ca.crt
cert client.crt
key client.key
remote-cert-tls client
tls-auth ta.key 1
cipher AES-256-CBC
# comp-lzo

verb 3

{{range $route := .Routes}}
route {{$route.Net}} {{$route.Mask}} {{$route.Gateway}}
{{ end }} 
`, data)
	})
}

func (c *ClientConfig) localPath(filename string) file.HasPath {
	return file.PathFunc(func(ctx context.Context) (string, error) {
		directory, err := c.clientDirectory()
		if err != nil {
			return "", err
		}
		return path.Join(directory, filename), nil
	})
}

func (c *ClientConfig) clientDirectory() (string, error) {
	usr, err := user.Current()
	if err != nil {
		return "", fmt.Errorf("get homedir failed: %w", err)
	}
	dir := filepath.Join(usr.HomeDir, ".openvpn", c.ClientName.String())
	if err := os.MkdirAll(dir, 0700); err != nil {
		return "", err
	}
	return dir, nil
}

func (c *ClientConfig) ClientKey() content.Func {
	return func(ctx context.Context) ([]byte, error) {
		caPrivKey, err := rsa.GenerateKey(rand.Reader, 4096)
		if err != nil {
			return nil, err
		}
		return pem.EncodeToMemory(&pem.Block{
			Type:  "RSA PRIVATE KEY",
			Bytes: x509.MarshalPKCS1PrivateKey(caPrivKey),
		}), nil
	}
}

func (c *ClientConfig) ClientCertifcate() *x509.Certificate {
	return &x509.Certificate{
		SerialNumber: big.NewInt(1658),
		Subject: pkix.Name{
			CommonName: c.ClientName.String(),
		},
		NotBefore:    time.Now(),
		NotAfter:     time.Now().AddDate(10, 0, 0),
		SubjectKeyId: []byte{1, 2, 3, 4, 6},
		ExtKeyUsage:  []x509.ExtKeyUsage{x509.ExtKeyUsageClientAuth, x509.ExtKeyUsageServerAuth},
		KeyUsage:     x509.KeyUsageDigitalSignature,
	}
}

func (c *ClientConfig) ClientCrt() content.Func {
	return func(ctx context.Context) ([]byte, error) {
		caPriv, err := readLocal(ctx, c.ServerConfig.LocalPathCAPrivateKey())
		if err != nil {
			return nil, err
		}

		caPrivPem, _ := pem.Decode(caPriv)
		if caPrivPem.Type != "RSA PRIVATE KEY" {
			return nil, fmt.Errorf("invalid type %s", caPrivPem.Type)
		}

		caPrivKey, err := x509.ParsePKCS1PrivateKey(caPrivPem.Bytes)
		if err != nil {
			return nil, err
		}

		certKey, err := readLocal(ctx, c.LocalPathClientKey())
		if err != nil {
			return nil, err
		}

		certPrivPem, _ := pem.Decode(certKey)
		if certPrivPem.Type != "RSA PRIVATE KEY" {
			return nil, fmt.Errorf("invalid type %s", certPrivPem.Type)
		}

		certPrivKey, err := x509.ParsePKCS1PrivateKey(certPrivPem.Bytes)
		if err != nil {
			return nil, err
		}

		certBytes, err := x509.CreateCertificate(
			rand.Reader,
			c.ClientCertifcate(),
			c.ServerConfig.CACertifcate(),
			&certPrivKey.PublicKey,
			caPrivKey,
		)
		if err != nil {
			return nil, err
		}

		return pem.EncodeToMemory(&pem.Block{
			Type:  "CERTIFICATE",
			Bytes: certBytes,
		}), nil
	}
}

func (c *ClientConfig) CaCrt() content.Func {
	return func(ctx context.Context) (bytes []byte, err error) {
		path, err := c.ServerConfig.LocalPathCaCrt().Path(ctx)
		if err != nil {
			return nil, err
		}
		return os.ReadFile(path)
	}
}

func (c *ClientConfig) TAKey() content.Func {
	return func(ctx context.Context) (bytes []byte, err error) {
		path, err := c.ServerConfig.LocalPathTaKey().Path(ctx)
		if err != nil {
			return nil, err
		}
		return os.ReadFile(path)
	}
}

func (c *ClientConfig) LocalPathTaKey() file.HasPath {
	return c.localPath("ta.key")
}

func (c *ClientConfig) LocalPathCaCrt() file.HasPath {
	return c.localPath("ca.crt")
}

func (c *ClientConfig) LocalPathClientKey() file.HasPath {
	return c.localPath("client.key")
}

func (c *ClientConfig) LocalPathClientCrt() file.HasPath {
	return c.localPath("client.crt")
}

func (c *ClientConfig) LocalPathConfig() file.HasPath {
	return c.localPath("client.ovpn")
}
