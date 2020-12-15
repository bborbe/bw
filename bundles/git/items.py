if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

actions = {}

for name, v in node.metadata.get('git', {}).get('clones', {}).items():
    repo = v.get('repo', '')
    if len(repo) == 0:
        raise Exception('git {} has no repo'.format(name))
    target = v.get('target', '')
    if len(target) == 0:
        raise Exception('git {} has no target'.format(name))

    actions['git_clone_{name}'.format(name=name)] = {
        'command': 'mkdir -p {target} && git clone -b {branch} --single-branch {repo} {target}'.format(branch=v.get('branch', 'master'), repo=repo, target=target),
        'unless': 'test -e {target}'.format(target=target),
        'needs': ['pkg_apt:git'],
    }

    actions['git_fetch_{name}'.format(name=name)] = {
        'command': 'git --git-dir {target}/.git fetch -p'.format(target=target),
        'needs': ['action:git_clone_{name}'.format(name=name)],
    }

    actions['git_checkout_{name}'.format(name=name)] = {
        'command': 'git --git-dir {target}/.git checkout {branch}'.format(branch=v.get('branch', 'master'), target=target),
        'needs': ['action:git_fetch_{name}'.format(name=name)],
    }

    actions['git_pull_{name}'.format(name=name)] = {
        'command': 'git --git-dir {target}/.git pull'.format(target=target),
        'needs': ['action:git_checkout_{name}'.format(name=name)],
    }
