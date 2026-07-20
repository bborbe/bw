defaults = {
    'bind': {
        'enabled': False,
        # bborbe/bind tag = {docker-bind git tag}-{yyyymm build stamp}. Built
        # manually from github.com/bborbe/docker-bind (make build upload) — the
        # legacy world tool rebuilt+pushed a fresh monthly stamp on every apply;
        # bw pins a fixed tag instead. https://hub.docker.com/r/bborbe/bind/tags
        'version': '1.4.1-202607',
    },
}
