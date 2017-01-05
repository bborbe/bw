if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

actions = {}

for k, v in node.metadata.get('git', {}).get('clones', {}).items():
    repo = v.get('repo', '')
    if len(repo) == 0:
        raise Exception('git {} has no repo'.format(k))
    target = v.get('target', '')
    if len(target) == 0:
        raise Exception('git {} has no target'.format(k))

    actions['git_clone_{name}'.format(name=k)] = {
        'command': 'mkdir -p {target} && git clone -b {branch} --single-branch {repo} {target}'.format(branch=v.get('branch', 'master'), repo=repo, target=target),
        'unless': 'test -e {target}'.format(target=target),
        'needs': ['pkg_apt:git'],
    }
