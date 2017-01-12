nodes['sm.tools'] = {
    'hostname': 'tools.seibert-media.net',
    'metadata': {
        'os': 'ubuntu',
        'release': 'xenial',
        'hosts': {
            'ipv4': {
                '138.201.37.217': ['tools.seibert-media.net', 'tools'],
            },
            'ipv6': {
                '2a01:4f8:171:3957::2': ['tools.seibert-media.net'],
            },
        },
        'kvm': {
            'enabled': True,
        },
        'grub': {
            'enabled': True,
        },
        'iptables': {
            'enabled': True,
            'nat_interfaces': ['eth0'],
            'rules': {
                'nat': [
                    # OpenVpn
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 563 -j DNAT --to-destination 172.16.10.3:563',
                    # Http + Https
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 80 -j DNAT --to-destination 172.16.10.2:1080',
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 443 -j DNAT --to-destination 172.16.10.2:1443',
                    # Minecraft
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 20001 -j DNAT --to-destination 172.16.11.15:30000',
                    # Mumble
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 64738 -j DNAT --to-destination 172.16.11.15:30019',
                    # Smtp + Smtps
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 25 -j DNAT --to-destination 172.16.11.15:30025',
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 465 -j DNAT --to-destination 172.16.11.15:30465',
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 587 -j DNAT --to-destination 172.16.11.15:30587',
                    # Imap + Imaps
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 143 -j DNAT --to-destination 172.16.11.15:30143',
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 993 -j DNAT --to-destination 172.16.11.15:30993',
                    # Ts3
                    '-A PREROUTING -i eth0 -p udp -d 138.201.37.217 --dport 9987 -j DNAT --to-destination 172.16.11.15:30087',
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 10011 -j DNAT --to-destination 172.16.11.15:30111',
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 30033 -j DNAT --to-destination 172.16.11.15:30033',
                    # Dns
                    '-A PREROUTING -i eth0 -p udp -d 138.201.37.217 --dport 53 -j DNAT --to-destination 172.16.11.15:30053',
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 53 -j DNAT --to-destination 172.16.11.15:30054',
                ],
                'filter': [
                    # Forward
                    '-A FORWARD -j ACCEPT',
                ],
            },
        },
        'users': {
            'kwiesmueller': {
                'sudo': True,
                'authorized_keys': {
                    'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCw8vSiSAbUSBR91lhWWM6C+a4+At1EtFs6c7IC7Rhp/SdkDvn4129OBkip8laKoa5A2iH0WMrZgYl8eulpYDeTnijqo4YziG5K6uX2g+MgJPwLfA6m5IT49Hrs5czEzIVHLIEtG2x8QqmgC9KRvBnoFVHlS0apF7C7KXuUYXSJ1q3WXtkxw3AE3LZEcAxw6klUzHYH0/TR1BrQe2kkq6NYN8mOTqF8Yq6aGXvysQWOBR6AMpQNx/raTvm4XJnuAATRR6SC/EIu2CLNUlKQSwhWjCOiEFsEIOD1yt1X+fzWjky0gTO+3thzwDUbAqY2UV5A3vZdPppJll9X5NTqInVqraViD6Z2YUSSwuRsTF230OqteoQB0K2qdCO19ltGKdpKGsVBybtMF9uMZC8McAR76S6PIVTapzG46WBMHmzL8MIxAcJ/cXvw2/6ZHsX8vTmYfNKYVf0j3W4oNVQBKk8M+3Lx+DFzRepAvZHsueFzPG5SLwEkIC46s6qgomW7WbDZf6wOfe5fUGspvNYb5RYytMsVW4g9QLs0G6QZvU06RFWqmHBx/JUU0j2V5dE3PPWcr3xBu7qb53NOw5QZ0Sogk/BUTpeR395gNbs/ybthoSDiWiZ3QR9AIKONRm3KDfzc6V3RsbxXESVJNThJt+kTfb2pqpp6JEt2w8zS9O2E8w== kwiesmueller@seibert-media.net': {},
                },
                'full_name': 'Kevin Wiesmueller',
            },
            'owolf': {
                'sudo': True,
                'authorized_keys': {
                    'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCcberdKUrK8fHp5Y1Wflg2Y1TPFN5bkwQe6LLvzSi4Qq3OFwNIxy//1HUjYbfGLLQbikH4kLLUJ1s/J5TPms++coISUMY7BGTVcpCISVi0ZpwR1uRqwSZA7OuF9PSyXkOUTLdVj0RlH3SB+xuOmDhVT6xlRWyLcjEQwikPV8915w1R44KBjzmiyn7nrPpK3sGlUPVpU54Z7ieAueMh9oDSCQBT/eLD8iEJ4sRyvc4Xrr81I5x4FT2L0uxcVG9Rm+JdUZUtMsy38c4Uso3gf4OvHhSWQfD4+Gu/PF3mJrRzxbQ9/Oi90FGj8reVHmtgDDWpDqOYkiWjbIZiXZLtHnJv owolf@seibert-media.net': {},
                },
                'full_name': 'Oliver Wolf',
            },
            'trehn': {
                'sudo': True,
                'authorized_keys': {
                    'ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAgEAtKhN971YtW3hcxKOK6I4A8Pzxu0SA5ydejyLQ6c9sx6OQklaSZyFMVYUi9l6p96uaVsDVGir4Y2vK1FgO+PqzLLFp8n1QSNO2ErVm1A7Yps60Y3I/2lHr4vIETkJ9EJkxjNvQsEPUAnn+vKButKUfkiqDie+2SIvG9MM/ZFmkJ3P+VBx5lDboPRi7h/Nb+4PvUE5vDDViAs6Slp2/wXEdvwwshRUXgjenAeAK58xhzasPow4dirN8LRmwZ1WRXcy2wvWALik9Wz7gltjoMLQbadDvZKTq7C6SZQgiwkHovwNhhiSJstKop5rLFVrkzyyVVDX5WBkKnBxv4DBZ7+IAR6esDYHW6e+Ojj7+VbOz0bUOn5pnmmGPTEKbc4tBRo8jTNNIx350JxdxN2rczrTtqZbzs3s1iHi6qO8za15XJW/c0Klqp0ZUIYhrMbaEYXqHdE16gMKmtYkp4XSa1h/bh+E94gv8USsuC+u4Yh7Sb9RzQMkl3G5ZE7Fw3T7ms6eOyqG4+d3ywp4EX+nWICHs/7pykEwQEt0lXTkjMdZ5II5mfEU01a/8msrjvHfJChjtSUk3W2GugFbU7X49z5HyluWBgyvLS/cWbce7+l+EoLM6nbzVGww53j6SyC0kSkDng+0t4d1QyCQAGvjG7QPPNU3xi4IJWHPSAh+ihzHIvM= trehn@seibert-media.net': {},
                },
                'full_name': 'Torsten Rehn',
            },
            'mschnitzius': {
                'sudo': True,
                'authorized_keys': {
                    'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDvhbDKHXMMGQcgoiBNLrl9O+trwtTT4LKZCzjsTLM+RdK5WNZdaHlR/Yfw7QS9SdIRzFP2ckzHHEc6bsne1ykeZimtUBzClawxZjq/U94s+n+y4VED8dHNXgCD/6s2+1tlbnaxvE4YdIvuGG6wDMF386fb1cIjJXWUhrTpK7bfWKYl8SoUlRNl+IZnPcslZ81ef0QKdgCyQlOdeCEbk2P+AGZcGp/bOYYu8raE8ueHElsXrgKq3WqC6HLdQOeqQUllANagQ+nmTlMS6qUwRlwMkR2Uuov9YuORBchNRyJdxZbiO/XMoY4mHksLiwP9Zcm8P3KNtSuGdn/oJ418+jVL mschnitzius@seibert-media.net': {},
                },
                'full_name': 'Marc Schnitzius',
            },
        },
    },
}
