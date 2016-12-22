os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

pkg_apt = {
    "git": {},
}

files = {}

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
