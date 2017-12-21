groups['user_group'] = {
    'member_patterns': (
        r'.*',
    ),
    'bundles': (
        'user',
    ),
    'metadata': {
        'users': {
            'root': {
                'enabled': True,
                'home': '/root',
            },
            'pi': {
                'enabled': False,
            },
            'ubuntu': {
                'enabled': False,
            },
            'bborbe': {
                'uid': '1000',
                'enabled': True,
                'sudo': True,
                'authorized_keys': {
                    'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCOw/yh7+j3ygZp2aZRdZDWUh0Dkj5N9/USdiLSoS+0CHJta+mtSxxmI/yv1nOk7xnuA6qtjpxdMlWn5obtC9xyS6T++tlTK9gaPwU7a/PObtoZdfQ7znAJDpX0IPI06/OH1tFE9kEutHQPzhCwRaIQ402BHIrUMWzzP7Ige8Oa0HwXH4sHUG5h/V/svzi9T0CKJjF8dTx4iUfKX959hT8wQnKYPULewkNBFv6pNfWIr8EzvIEQcPmmm3tP+dQPKg5QKVi6jPdRla+t5HXfhXu0W3WCDa2s0VGmJjBdMMowr5MLNYI79MKziSV1w1IWL17Z58Lop0zEHqP7Ba0Aooqd': {},
                },
                'full_name': 'Benjamin Borbe',
                'dotfiles': 'https://github.com/bborbe/dotfiles.git',
            },
            'jana': {
                'uid': '1001',
                'full_name': 'Jana Borbe',
            },
            'walter': {
                'uid': '1002',
                'full_name': 'Walter Borbe',
            },
            'brigitte': {
                'uid': '1003',
                'full_name': 'Brigitte Borbe',
            },
            'kristin': {
                'uid': '1004',
                'full_name': 'Kristin Borbe',
            },
            'kwiesmueller': {
                'uid': '1005',
                'sudo': True,
                'authorized_keys': {
                    'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCw8vSiSAbUSBR91lhWWM6C+a4+At1EtFs6c7IC7Rhp/SdkDvn4129OBkip8laKoa5A2iH0WMrZgYl8eulpYDeTnijqo4YziG5K6uX2g+MgJPwLfA6m5IT49Hrs5czEzIVHLIEtG2x8QqmgC9KRvBnoFVHlS0apF7C7KXuUYXSJ1q3WXtkxw3AE3LZEcAxw6klUzHYH0/TR1BrQe2kkq6NYN8mOTqF8Yq6aGXvysQWOBR6AMpQNx/raTvm4XJnuAATRR6SC/EIu2CLNUlKQSwhWjCOiEFsEIOD1yt1X+fzWjky0gTO+3thzwDUbAqY2UV5A3vZdPppJll9X5NTqInVqraViD6Z2YUSSwuRsTF230OqteoQB0K2qdCO19ltGKdpKGsVBybtMF9uMZC8McAR76S6PIVTapzG46WBMHmzL8MIxAcJ/cXvw2/6ZHsX8vTmYfNKYVf0j3W4oNVQBKk8M+3Lx+DFzRepAvZHsueFzPG5SLwEkIC46s6qgomW7WbDZf6wOfe5fUGspvNYb5RYytMsVW4g9QLs0G6QZvU06RFWqmHBx/JUU0j2V5dE3PPWcr3xBu7qb53NOw5QZ0Sogk/BUTpeR395gNbs/ybthoSDiWiZ3QR9AIKONRm3KDfzc6V3RsbxXESVJNThJt+kTfb2pqpp6JEt2w8zS9O2E8w==': {},
                },
                'full_name': 'Kevin Wiesmueller',
                'generate_password': True,
            },
            'owolf': {
                'uid': '1006',
                'sudo': True,
                'authorized_keys': {
                    'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCcberdKUrK8fHp5Y1Wflg2Y1TPFN5bkwQe6LLvzSi4Qq3OFwNIxy//1HUjYbfGLLQbikH4kLLUJ1s/J5TPms++coISUMY7BGTVcpCISVi0ZpwR1uRqwSZA7OuF9PSyXkOUTLdVj0RlH3SB+xuOmDhVT6xlRWyLcjEQwikPV8915w1R44KBjzmiyn7nrPpK3sGlUPVpU54Z7ieAueMh9oDSCQBT/eLD8iEJ4sRyvc4Xrr81I5x4FT2L0uxcVG9Rm+JdUZUtMsy38c4Uso3gf4OvHhSWQfD4+Gu/PF3mJrRzxbQ9/Oi90FGj8reVHmtgDDWpDqOYkiWjbIZiXZLtHnJv owolf@seibert-media.net': {},
                },
                'full_name': 'Oliver Wolf',
                'generate_password': True,
            },
            'trehn': {
                'uid': '1007',
                'sudo': True,
                'authorized_keys': {
                    'ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAgEAtKhN971YtW3hcxKOK6I4A8Pzxu0SA5ydejyLQ6c9sx6OQklaSZyFMVYUi9l6p96uaVsDVGir4Y2vK1FgO+PqzLLFp8n1QSNO2ErVm1A7Yps60Y3I/2lHr4vIETkJ9EJkxjNvQsEPUAnn+vKButKUfkiqDie+2SIvG9MM/ZFmkJ3P+VBx5lDboPRi7h/Nb+4PvUE5vDDViAs6Slp2/wXEdvwwshRUXgjenAeAK58xhzasPow4dirN8LRmwZ1WRXcy2wvWALik9Wz7gltjoMLQbadDvZKTq7C6SZQgiwkHovwNhhiSJstKop5rLFVrkzyyVVDX5WBkKnBxv4DBZ7+IAR6esDYHW6e+Ojj7+VbOz0bUOn5pnmmGPTEKbc4tBRo8jTNNIx350JxdxN2rczrTtqZbzs3s1iHi6qO8za15XJW/c0Klqp0ZUIYhrMbaEYXqHdE16gMKmtYkp4XSa1h/bh+E94gv8USsuC+u4Yh7Sb9RzQMkl3G5ZE7Fw3T7ms6eOyqG4+d3ywp4EX+nWICHs/7pykEwQEt0lXTkjMdZ5II5mfEU01a/8msrjvHfJChjtSUk3W2GugFbU7X49z5HyluWBgyvLS/cWbce7+l+EoLM6nbzVGww53j6SyC0kSkDng+0t4d1QyCQAGvjG7QPPNU3xi4IJWHPSAh+ihzHIvM=': {},
                },
                'full_name': 'Torsten Rehn',
                'generate_password': True,
            },
            'star': {
                'uid': '1008',
            },
            'nova': {
                'uid': '1009',
            },
            'borbe': {
                'uid': '1010',
            },
            'bkendinibilir': {
                'uid': '1011',
                'sudo': True,
                'authorized_keys': {
                    'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDPT4V+S3OglvXEHkpJA85oCmES/iOoAn/ju06xzQhH7GjT86uuEjbnQ8eFQ8l8wm+HvEwhMm0uFfqjUmABCYhH4kOhWPPwCMBZCWFtRQ4yMuPAXBTytWS5wTufK+ALuLVBBmWKA7yPaJeLTKUjhWXJaauKCrA5VK22vx4Sg2HqXziaJYXTgZe4e5oumFsiCxd7sfJrkWV0mApSfWqw/2qfA37Jdb8Fr+OSujJdIaPUaPhqxH8kPM/g5HLS2VneBCvYhi6AFmuYd+Y2s8IacZkjmifoKQKh9LP36gLB/Nn64xW6ztvgXrSjPvXUdUTPEtPoJZPQy2be3K5MZcwjvl6UWpUVUhOeGeNI0wvqPRVzVW/DcKFzaly2g8eO0YGhHG+HSufFA5KeBs3ygP5Fpu/MlrgobV5QV6LTLW80sPXnlt8yfcIUnXjkucv8cncjDhOuHko5L70B9MqO93f1r+uvmeHymTYceRKobSn+TK0wkocAojENLzPYdZcPheTCL0GFlp0Nbtuz7jm+A3jZaOq5v7lRCI0YPdTP/sMs6IXcsNa/3NPQTf/UI/d4qJXXoEhPY6OyLe9CdJ0MiNnNoG+PGiDlRISLnT+AGVUZBiNnIvYXFWA0bKqqrzpGNHOQgHwABp/nRBwx4qPIBfR4bob+/es3cFxluCLN4X/gUdXYtQ==': {},
                },
                'full_name': 'Benjamin Kendinibilir',
                'generate_password': True,
            },
            'mschnitzius': {
                'uid': '1012',
                'sudo': True,
                'authorized_keys': {
                    'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDvhbDKHXMMGQcgoiBNLrl9O+trwtTT4LKZCzjsTLM+RdK5WNZdaHlR/Yfw7QS9SdIRzFP2ckzHHEc6bsne1ykeZimtUBzClawxZjq/U94s+n+y4VED8dHNXgCD/6s2+1tlbnaxvE4YdIvuGG6wDMF386fb1cIjJXWUhrTpK7bfWKYl8SoUlRNl+IZnPcslZ81ef0QKdgCyQlOdeCEbk2P+AGZcGp/bOYYu8raE8ueHElsXrgKq3WqC6HLdQOeqQUllANagQ+nmTlMS6qUwRlwMkR2Uuov9YuORBchNRyJdxZbiO/XMoY4mHksLiwP9Zcm8P3KNtSuGdn/oJ418+jVL': {},
                },
                'full_name': 'Marc Schnitzius',
                'generate_password': True,
            },
            'mfrankl': {
                'uid': '1013',
                'sudo': True,
                'authorized_keys': {
                    'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQCbSV6p4gdUO3/HOTRfDYnDHgLFSy5ROXBb8FhCfRYhPgGfC8tNMLUt9HB96DEWHnPDFhKujLnDyFP5SjBbUKFp2Mz9ff+rmQxjtW6hT2ZunYt6pOKWGrKiOCqIaANZNhLDBBV54lfs/m2s4dfGhJcMfhNgtDUheT31+OhOFja8JQ==': {},
                },
                'full_name': 'Michael Frankl',
                'generate_password': True,
            },
            'sjanusch': {
                'uid': '1014',
                'sudo': True,
                'authorized_keys': {
                    'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAxngOdolLkGr8Epeh5+F4uYdB2cpSdnlQyw59Pow2DFSy+SJ8zo/DnXZDE2dTBN72FNaal4LvTh8WVnCs/T7t6kI+0hcvEWHycCyav5feLUyUWz+Lh9amVLJbXMPr8jLVhjo2wa9IOL5C3N3VcKb8jrZ74LsnZ/fP3qbjGojTLSRh93CCCJDB73J0RfoQH7GkbJkBN8qhdK8xv4fqqiebKJKUtPuMtInWNOiMisUsd5NL8VwsLU2BOhJVPngzRCRftTUIVYZMNX/Iz7d5s4zEOPU5ybwvMVV0FvKr4RgBB2+zdnEduJN94ygXVPD9G0e5ti+02TovwEyvANbmNpDv': {},
                },
                'full_name': 'Sandro Janusch',
                'generate_password': True,
            },
            'openhab': {
                'uid': '1015',
            },
        },
        'groups': {
            'bborbe': {
                'gid': '1000',
            },
            'jana': {
                'gid': '1001',
            },
            'walter': {
                'gid': '1002',
            },
            'brigitte': {
                'gid': '1003',
            },
            'kristin': {
                'gid': '1004',
            },
            'kwiesmueller': {
                'gid': '1005',
            },
            'owolf': {
                'gid': '1006',
            },
            'trehn': {
                'gid': '1007',
            },
            'star': {
                'gid': '1008',
            },
            'nova': {
                'gid': '1009',
            },
            'borbe': {
                'gid': '1010',
            },
            'bkendinibilir': {
                'gid': '1011',
            },
            'mschnitzius': {
                'gid': '1012',
            },
            'mfrankl': {
                'gid': '1013',
            },
            'sjanusch': {
                'gid': '1014',
            },
            'openhab': {
                'gid': '1015',
            },
            'data': {
                'gid': '2000',
            },
        },
    },
}
