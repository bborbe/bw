// Copyright (c) 2019 Benjamin Borbe All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package openvpn

import (
	"bytes"
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
	"os/exec"
	"os/user"
	"path"
	"path/filepath"
	"time"

	"github.com/bborbe/world/pkg/content"
	"github.com/bborbe/world/pkg/file"
	"github.com/bborbe/world/pkg/network"
	"github.com/bborbe/world/pkg/template"
	"github.com/bborbe/world/pkg/validation"
)

type ServerConfig struct {
	ServerName  ServerName
	ServerIPNet network.IPNet
	ServerPort  network.Port
	Routes      Routes
	Device      Device
}

func (s ServerConfig) Validate(ctx context.Context) error {
	return validation.Validate(
		ctx,
		s.ServerName,
		s.ServerIPNet,
		s.Routes,
		s.ServerPort,
		s.Device,
	)
}

func (s *ServerConfig) OpenvpnDefaultConf() content.Func {
	return func(ctx context.Context) ([]byte, error) {
		return []byte(`
AUTOSTART="all"
OPTARGS=""
OMIT_SENDSIGS=0
`), nil
	}
}

func (s *ServerConfig) ServerConfigContent() content.Func {
	return func(ctx context.Context) ([]byte, error) {
		serverIPNet, err := s.ServerIPNet.IPNet(ctx)
		if err != nil {
			return nil, err
		}

		port, err := s.ServerPort.Port(ctx)
		if err != nil {
			return nil, err
		}

		type Route struct {
			Gateway string
			Net     string
			Mask    string
		}
		data := struct {
			ServerIP      string
			ServerNetmask string
			ServerPort    int
			Routes        []Route
			Device        string
		}{
			ServerIP:      serverIPNet.IP.String(),
			ServerNetmask: net.IP(serverIPNet.Mask).String(),
			ServerPort:    port,
			Routes:        []Route{},
			Device:        s.Device.String(),
		}
		for _, route := range s.Routes {
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
dev {{.Device}}
port {{.ServerPort}}
proto tcp4
server {{.ServerIP}} {{.ServerNetmask}}
ca /etc/openvpn/keys/ca.crt
cert /etc/openvpn/keys/server.crt
key /etc/openvpn/keys/server.key
dh /etc/openvpn/keys/dh.pem
tls-auth /etc/openvpn/keys/ta.key 0
ifconfig-pool-persist ip_pool
keepalive 10 120
cipher AES-256-CBC
persist-key
persist-tun
status server.status
topology subnet
# comp-lzo
client-config-dir /etc/openvpn/ccd
push "route {{.ServerIP}} {{.ServerNetmask}}"
client-to-client

# route to 192.168.178.0/24 via opnsense 
route 192.168.178.0 255.255.255.0 172.16.90.10

verb 3
log /var/log/openvpn/server.log

{{range $route := .Routes}}
route {{$route.Net}} {{$route.Mask}} {{$route.Gateway}}
{{ end }} 
`, data)
	}
}

func (s *ServerConfig) CAPrivateKey() content.Func {
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

func (s *ServerConfig) CACertifcate() *x509.Certificate {
	return &x509.Certificate{
		SerialNumber: big.NewInt(2019),
		Subject: pkix.Name{
			Organization:  []string{"Benjamin Borbe"},
			Country:       []string{"DE"},
			Province:      []string{"Hessen"},
			Locality:      []string{"Wiesbaden"},
			StreetAddress: []string{""},
			PostalCode:    []string{""},
		},
		NotBefore: time.Now(),
		NotAfter:  time.Now().AddDate(10, 0, 0),
		IsCA:      true,
		ExtKeyUsage: []x509.ExtKeyUsage{
			x509.ExtKeyUsageClientAuth,
			x509.ExtKeyUsageServerAuth,
		},
		KeyUsage:              x509.KeyUsageDigitalSignature | x509.KeyUsageCertSign,
		BasicConstraintsValid: true,
	}
}

func (s *ServerConfig) CaCrt() content.Func {
	return func(ctx context.Context) ([]byte, error) {
		caPriv, err := readLocal(ctx, s.LocalPathCAPrivateKey())
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

		caCert, err := x509.CreateCertificate(
			rand.Reader,
			s.CACertifcate(),
			s.CACertifcate(),
			&caPrivKey.PublicKey,
			caPrivKey,
		)
		if err != nil {
			return nil, err
		}

		return pem.EncodeToMemory(&pem.Block{
			Type:  "CERTIFICATE",
			Bytes: caCert,
		}), nil
	}
}

func (s *ServerConfig) ServerCertifcate() *x509.Certificate {
	return &x509.Certificate{
		SerialNumber: big.NewInt(1658),
		Subject: pkix.Name{
			CommonName: s.ServerName.String(),
		},
		NotBefore:    time.Now(),
		NotAfter:     time.Now().AddDate(10, 0, 0),
		SubjectKeyId: []byte{1, 2, 3, 4, 6},
		ExtKeyUsage:  []x509.ExtKeyUsage{x509.ExtKeyUsageClientAuth, x509.ExtKeyUsageServerAuth},
		KeyUsage:     x509.KeyUsageDigitalSignature,
	}
}

func (s *ServerConfig) ServerCrt() content.Func {
	return func(ctx context.Context) ([]byte, error) {
		caPriv, err := readLocal(ctx, s.LocalPathCAPrivateKey())
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

		certKey, err := readLocal(ctx, s.LocalPathServerKey())
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
			s.ServerCertifcate(),
			s.CACertifcate(),
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

func (s *ServerConfig) ServerKey() content.Func {
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

func (s *ServerConfig) TAKey() content.Func {
	return func(ctx context.Context) ([]byte, error) {
		buf := &bytes.Buffer{}
		command := exec.CommandContext(ctx, "openvpn2", "--genkey", "--secret", "/dev/stdout")
		command.Stdout = buf
		err := command.Run()
		if err != nil {
			return nil, err
		}
		return buf.Bytes(), nil
	}
}

func (s *ServerConfig) DHPem() content.Func {
	return func(ctx context.Context) ([]byte, error) {
		buf := &bytes.Buffer{}
		command := exec.CommandContext(ctx, "openssl", "dhparam", "-out", "-", "1024")
		command.Stdout = buf
		err := command.Run()
		if err != nil {
			return nil, err
		}
		return buf.Bytes(), nil
	}
}

func (s *ServerConfig) LocalPathCaCrt() file.HasPath {
	return s.localPath("ca.crt")
}

func (s *ServerConfig) LocalPathCAPrivateKey() file.HasPath {
	return s.localPath("ca.key")
}

func (s *ServerConfig) LocalPathServerCrt() file.HasPath {
	return s.localPath("server.crt")
}

func (s *ServerConfig) LocalPathDhPem() file.HasPath {
	return s.localPath("dh.pem")
}

func (s *ServerConfig) LocalPathTaKey() file.HasPath {
	return s.localPath("ta.key")
}

func (s *ServerConfig) LocalPathServerKey() file.HasPath {
	return s.localPath("server.key")
}

func (s *ServerConfig) serverDirectory() (string, error) {
	usr, err := user.Current()
	if err != nil {
		return "", fmt.Errorf("get homedir failed: %w", err)
	}
	dir := filepath.Join(usr.HomeDir, ".openvpn", s.ServerName.String())
	if err := os.MkdirAll(dir, 0700); err != nil {
		return "", err
	}
	return dir, nil
}

func (s *ServerConfig) localPath(filename string) file.HasPath {
	return file.PathFunc(func(ctx context.Context) (string, error) {
		directory, err := s.serverDirectory()
		if err != nil {
			return "", err
		}
		return path.Join(directory, filename), nil
	})
}

func readLocal(ctx context.Context, path file.HasPath) ([]byte, error) {
	filename, err := path.Path(ctx)
	if err != nil {
		return nil, err
	}
	return os.ReadFile(filename)
}
