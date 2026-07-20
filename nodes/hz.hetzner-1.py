import bwtv as teamvault

nodes['hz.hetzner-1'] = {
    'hostname': 'hetzner-1.benjamin-borbe.de',
    'groups': {
        'ubuntu-noble',
    },
    'metadata': {
        'conduit-server': {
            'enabled': True,
            'server_name': 'matrix.benjamin-borbe.de',
            'well_known_base_domain': 'benjamin-borbe.de',
            'well_known_ip': '159.69.203.89',
        },
        'lockbox': {
            'enabled': True,
            'version': 'v0.8.0',
            'port': 8091,
            'encryption_key': teamvault.password('VO05mL', site='benjamin-borbe'),
            'basic_auth_user': teamvault.username('7qGnWL', site='benjamin-borbe'),
            'basic_auth_pass': teamvault.password('7qGnWL', site='benjamin-borbe'),
        },
        'docker': {
            'enabled': True,
        },
        'backup_client': {
            'enabled': True,
        },
        'netplan': {
            'enabled': True,
            'ethernets': {
                'eth0': {
                    'dhcp4': True,
                    'dhcp6': False,
                },
            },
        },
        'screego': {
            'enabled': True,
            'version': '1.12.4',
            'external_ip': '159.69.203.89',
            'secret': teamvault.password('xwXMpO', site='benjamin-borbe'),
            'users_file': teamvault.password('Rwgzeq', site='benjamin-borbe'),
        },
        'ip': {
            'enabled': True,
            'version': '1.1.0',
            'port': 8000,
        },
        'poste': {
            'enabled': True,
            'version': '2.5.13-2.0.1',
            'admin_port': 8001,
        },
        'bind': {
            'enabled': True,
            'version': '1.4.1-202607',
        },
        'nginx': {
            'enabled': True,
            'vhosts': {
                'kickstart': {
                    'ip': '159.69.203.89',
                    'root': '/var/lib/kickstart',
                    'locations': {
                        '/': {
                            'autoindex': 'on',
                        },
                    },
                    'server_names': [
                        'kickstart.benjamin-borbe.de',
                        'ks.benjamin-borbe.de',
                    ],
                    'ssl': {
                        'force': False,
                        'cert': '/etc/letsencrypt/live/kickstart.benjamin-borbe.de/fullchain.pem',
                        'key': '/etc/letsencrypt/live/kickstart.benjamin-borbe.de/privkey.pem',
                    },
                    'indexes': [],
                },
                'matrix': {
                    'ip': '159.69.203.89',
                    'server_names': [
                        'matrix.benjamin-borbe.de',
                    ],
                    'ssl': {
                        'force': True,
                        'cert': '/etc/letsencrypt/live/matrix.benjamin-borbe.de/fullchain.pem',
                        'key': '/etc/letsencrypt/live/matrix.benjamin-borbe.de/privkey.pem',
                    },
                    'locations': {
                        '/': {
                            'proxy_pass': 'http://127.0.0.1:8448',
                            'proxy_set_header Host': '$host',
                            'proxy_set_header X-Real-IP': '$remote_addr',
                        },
                    },
                    'indexes': [],
                },
                'lockbox': {
                    'ip': '159.69.203.89',
                    'server_names': [
                        'lockbox.benjamin-borbe.de',
                    ],
                    'ssl': {
                        'force': True,
                        'cert': '/etc/letsencrypt/live/lockbox.benjamin-borbe.de/fullchain.pem',
                        'key': '/etc/letsencrypt/live/lockbox.benjamin-borbe.de/privkey.pem',
                    },
                    'locations': {
                        '/': {
                            'proxy_pass': 'http://127.0.0.1:8091',
                            'proxy_set_header Host': '$host',
                            'proxy_set_header X-Real-IP': '$remote_addr',
                        },
                    },
                    'indexes': [],
                },
                'ip': {
                    'ip': '159.69.203.89',
                    'server_names': [
                        'ip.benjamin-borbe.de',
                    ],
                    'ssl': {
                        'force': True,
                        'cert': '/etc/letsencrypt/live/ip.benjamin-borbe.de/fullchain.pem',
                        'key': '/etc/letsencrypt/live/ip.benjamin-borbe.de/privkey.pem',
                    },
                    'locations': {
                        '/': {
                            'proxy_pass': 'http://127.0.0.1:8000',
                            'proxy_set_header Host': '$host',
                            'proxy_set_header X-Real-IP': '$remote_addr',
                        },
                    },
                    'indexes': [],
                },
                'screego': {
                    'ip': '159.69.203.89',
                    'server_names': [
                        'screen.benjamin-borbe.de',
                    ],
                    'ssl': {
                        'force': True,
                        'cert': '/etc/letsencrypt/live/screen.benjamin-borbe.de/fullchain.pem',
                        'key': '/etc/letsencrypt/live/screen.benjamin-borbe.de/privkey.pem',
                    },
                    'locations': {
                        '/': {
                            'proxy_pass': 'http://127.0.0.1:5050',
                            'proxy_set_header Host': '$host',
                            'proxy_set_header X-Real-IP': '$remote_addr',
                            'proxy_set_header Upgrade': '$http_upgrade',
                            'proxy_set_header Connection': 'upgrade',
                        },
                    },
                    'indexes': [],
                },
                'teamvault': {
                    'ip': '159.69.203.89',
                    'server_names': [
                        'teamvault.benjamin-borbe.de',
                    ],
                    'ssl': {
                        'force': True,
                        'cert': '/etc/letsencrypt/live/teamvault.benjamin-borbe.de/fullchain.pem',
                        'key': '/etc/letsencrypt/live/teamvault.benjamin-borbe.de/privkey.pem',
                    },
                    'locations': {
                        # Proxies to the TeamVault backend on nuke-k3s-prod-worker-0
                        # (192.168.178.44), reachable from this cloud host over the
                        # OpenVPN tunnel. client_max_body_size (100M) is set at
                        # location scope (valid nginx) to allow TeamVault file uploads.
                        '/': {
                            'client_max_body_size': '100M',
                            'proxy_pass': 'http://192.168.178.44/',
                            'proxy_set_header Host': '$host',
                            'proxy_set_header X-Forwarded-Host': '$host:$server_port',
                            'proxy_set_header X-Forwarded-Server': '$host',
                            'proxy_set_header X-Forwarded-For': '$proxy_add_x_forwarded_for',
                            'proxy_set_header X-Forwarded-Proto': 'https',
                        },
                    },
                    'indexes': [],
                },
                'mail': {
                    'ip': '159.69.203.89',
                    'server_names': [
                        'mail.benjamin-borbe.de',
                    ],
                    'ssl': {
                        'force': True,
                        'cert': '/etc/letsencrypt/live/mail.benjamin-borbe.de/fullchain.pem',
                        'key': '/etc/letsencrypt/live/mail.benjamin-borbe.de/privkey.pem',
                    },
                    'locations': {
                        # poste.io mail UI (still served by world's poste container on
                        # localhost:8001 until the poste service itself is migrated).
                        '/': {
                            'client_max_body_size': '100M',
                            'proxy_pass': 'http://localhost:8001/',
                            'proxy_set_header Host': '$host',
                            'proxy_set_header X-Forwarded-Host': '$host:$server_port',
                            'proxy_set_header X-Forwarded-Server': '$host',
                            'proxy_set_header X-Forwarded-For': '$proxy_add_x_forwarded_for',
                            'proxy_set_header X-Forwarded-Proto': 'https',
                        },
                    },
                    'indexes': [],
                },
                'quant': {
                    'ip': '159.69.203.89',
                    'server_names': [
                        'quant.benjamin-borbe.de',
                    ],
                    'ssl': {
                        'force': True,
                        'cert': '/etc/letsencrypt/live/quant.benjamin-borbe.de/fullchain.pem',
                        'key': '/etc/letsencrypt/live/quant.benjamin-borbe.de/privkey.pem',
                    },
                    'locations': {
                        # Website gateway on nuke-k3s-prod-worker-0 (192.168.178.44) over the
                        # VPN — same as the teamvault vhost. The .37/.44 cluster's traefik
                        # LoadBalancer advertises only the LAN IP, reached via the iroute
                        # 192.168.178.44/32 in the worker's openvpn ccd. Migrated off the old
                        # backend_servers upstream (still used by dev.quant/prod.quant trading UIs).
                        '/': {
                            'client_max_body_size': '100M',
                            'proxy_pass': 'http://192.168.178.44',
                            'proxy_http_version': '1.1',
                            'proxy_set_header Host': '$host',
                            'proxy_set_header X-Forwarded-Host': '$host:$server_port',
                            'proxy_set_header X-Forwarded-Server': '$host',
                            'proxy_set_header X-Forwarded-For': '$proxy_add_x_forwarded_for',
                            'proxy_set_header X-Forwarded-Proto': 'https',
                            'proxy_set_header Upgrade': '$http_upgrade',
                            'proxy_set_header Connection': 'upgrade',
                            'access_log': '/var/log/nginx/quant.benjamin-borbe.de-access.log combined',
                        },
                    },
                    'indexes': [],
                },
                'dev.quant': {
                    'ip': '159.69.203.89',
                    'server_names': [
                        'dev.quant.benjamin-borbe.de',
                    ],
                    'ssl': {
                        'force': True,
                        'cert': '/etc/letsencrypt/live/dev.quant.benjamin-borbe.de/fullchain.pem',
                        'key': '/etc/letsencrypt/live/dev.quant.benjamin-borbe.de/privkey.pem',
                    },
                    'locations': {
                        # Proxies to the backend_servers upstream, with websocket +
                        # streaming timeouts and buffering off.
                        '/': {
                            'client_max_body_size': '100M',
                            'proxy_pass': 'http://backend_servers',
                            'proxy_http_version': '1.1',
                            'proxy_set_header Host': '$host',
                            'proxy_set_header X-Forwarded-Host': '$host:$server_port',
                            'proxy_set_header X-Forwarded-Server': '$host',
                            'proxy_set_header X-Forwarded-For': '$proxy_add_x_forwarded_for',
                            'proxy_set_header X-Forwarded-Proto': 'https',
                            'proxy_set_header Upgrade': '$http_upgrade',
                            'proxy_set_header Connection': 'upgrade',
                            'proxy_read_timeout': '300s',
                            'proxy_connect_timeout': '60s',
                            'proxy_send_timeout': '300s',
                            'proxy_buffering': 'off',
                            'proxy_cache': 'off',
                        },
                    },
                    'indexes': [],
                },
                'prod.quant': {
                    'ip': '159.69.203.89',
                    'server_names': [
                        'prod.quant.benjamin-borbe.de',
                    ],
                    'ssl': {
                        'force': True,
                        'cert': '/etc/letsencrypt/live/prod.quant.benjamin-borbe.de/fullchain.pem',
                        'key': '/etc/letsencrypt/live/prod.quant.benjamin-borbe.de/privkey.pem',
                    },
                    'locations': {
                        # Production trading UI — proxies to the backend_servers upstream,
                        # websocket + streaming timeouts and buffering off.
                        '/': {
                            'client_max_body_size': '100M',
                            'proxy_pass': 'http://backend_servers',
                            'proxy_http_version': '1.1',
                            'proxy_set_header Host': '$host',
                            'proxy_set_header X-Forwarded-Host': '$host:$server_port',
                            'proxy_set_header X-Forwarded-Server': '$host',
                            'proxy_set_header X-Forwarded-For': '$proxy_add_x_forwarded_for',
                            'proxy_set_header X-Forwarded-Proto': 'https',
                            'proxy_set_header Upgrade': '$http_upgrade',
                            'proxy_set_header Connection': 'upgrade',
                            'proxy_read_timeout': '300s',
                            'proxy_connect_timeout': '60s',
                            'proxy_send_timeout': '300s',
                            'proxy_buffering': 'off',
                            'proxy_cache': 'off',
                        },
                    },
                    'indexes': [],
                },
                'webdav': {
                    'ip': '159.69.203.89',
                    'server_names': [
                        'webdav.benjamin-borbe.de',
                    ],
                    'root': '/home/webdav',
                    'ssl': {
                        'force': True,
                        'cert': '/etc/letsencrypt/live/webdav.benjamin-borbe.de/fullchain.pem',
                        'key': '/etc/letsencrypt/live/webdav.benjamin-borbe.de/privkey.pem',
                    },
                    'locations': {
                        # WebDAV over /home/webdav. dav_ext_methods needs the
                        # libnginx-mod-http-dav-ext package (installed by the nginx
                        # bundle). auth_basic htpasswd is rendered from TeamVault
                        # (see htpasswd_files below).
                        '/': {
                            'client_max_body_size': '100M',
                            'autoindex': 'on',
                            'dav_methods': 'PUT DELETE MKCOL COPY MOVE',
                            'dav_ext_methods': 'PROPFIND OPTIONS',
                            'auth_basic': '"Restricted area"',
                            'auth_basic_user_file': '/etc/nginx/webdav.htpasswd',
                        },
                    },
                    'indexes': [],
                },
            },
            'htpasswd_files': {
                # webdav auth_basic user file (user:hash) from TeamVault.
                '/etc/nginx/webdav.htpasswd': teamvault.password('NqAE5q', site='benjamin-borbe'),
            },
            'upstreams': {
                # nuke cluster backend (over the OpenVPN tunnel) behind the quant vhosts.
                # No explicit health-check directives — faithful to world's original
                # backend-server.conf. nginx applies its default passive checks
                # (max_fails=1, fail_timeout=10s) and default proxy_next_upstream, so a
                # dead backend is marked down and retried. Explicit active health-checks
                # would be a deliberate behavior change, out of scope for this migration.
                'backend_servers': [
                    '172.16.90.6',
                    '172.16.90.7',
                    '172.16.90.9',
                ],
            },
        },
        'golang': {
            'enabled': True,
            'arch': 'amd64',
            'os': 'linux',
        },
        'iptables': {
            'enabled': True,
            'nat_interfaces': [],
            'rules': {
                'filter': {
                    # allow forward
                    # '-A FORWARD -j ACCEPT',
                    # '-A FORWARD -i tun0 -o tun0 -j DROP',
                    '-A FORWARD -i tun0 -o eth0 -j ACCEPT',
                    '-A FORWARD -i eth0 -o tun0 -m state --state RELATED,ESTABLISHED -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 25 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 53 -j ACCEPT',
                    '-A INPUT -p udp -m state --state NEW -m udp --dport 53 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 80 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 143 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 443 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 465 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 563 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 587 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 993 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 2222 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 3128 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 6443 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 64738 -j ACCEPT',
                },
            },
        },
        'users': {
            'bborbe': {
                'enabled': True,
            },
            # Service account matching the screego container's non-root UID (1001),
            # so bw can own the secret files by name and read back a resolvable owner.
            'screego': {
                'enabled': True,
                'uid': 1001,
                'shell': '/usr/sbin/nologin',
            },
        },
    },
}
