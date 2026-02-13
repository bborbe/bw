# Changelog

All notable changes to this project will be documented in this file.

Please choose versions by [Semantic Versioning](http://semver.org/).

* MAJOR version when you make incompatible API changes,
* MINOR version when you add functionality in a backwards-compatible manner, and
* PATCH version when you make backwards-compatible bug fixes.

## v0.3.4
- Add GitHub Actions CI workflow for automated testing
- Add openclaw user to nuke-boss node

## v0.3.3
- Improve Docker build cache GC policy with aggressive cleanup rules (10GB limit, 7-day retention)

## v0.3.2
- Add automatic Docker build cache cleanup with 20GB limit to daemon.json

## v0.3.1
- Add hetzner-2 node with docker, nginx, and SSL configuration for OpenClaw

## v0.3.0
- Add workspace bundle with development tools (gnupg2, build-essential, git, direnv, ripgrep, etc.)
- Enable workspace on hm.fire, hm.sun, and hm.nuke-workspace nodes
- Update golang to 1.25.7
- Add ripgrep to meta-bundles
- Add disk configuration for nuke-workspace

## v0.2.1
- Update bundlewrap to 4.24.0
- Update bundlewrap-teamvault to 3.1.5
- Remove transitive dependencies from requirements.txt

## v0.2.0
- Add trivy bundle to meta-bundles group
- Enable trivy on nuke-workspace node

## v0.1.3
- Update golang default version to 1.25.6
- Enable golang on nuke-workspace

## v0.1.2
- Add docker group to bborbe user on nuke-workspace

## v0.1.1
- Move kubectl from node-specific bundle to meta-bundles group

## v0.1.0
- Add kubectl bundle with modern signed-by keyring pattern
- Enable kubectl on nuke-workspace node

## v0.0.1
- Initial release
