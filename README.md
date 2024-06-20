# BundleWrap Configuration

This repo contains my BundleWrap configuration. For more info about BundleWrap see: [http://bundlewrap.org/](http://BundleWrap.org/).

## Upgrade requirements.txt

```bash
pip install pip-upgrader
pip-upgrade
```

## Install pyenv

```bash
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
```

## Update pyenv versions

```bash
cd ~/.pyenv/plugins/python-build/../.. && git pull && cd -
```

## Install Python

```bash
pyenv install 3.10.14
```

## Install pyenv-virtualenv

```bash
    git clone https://github.com/yyuu/pyenv-virtualenv
cd pyenv-virtualenv
sudo ./install.sh
```

## Create Bundlewrap env

```bash
pyenv virtualenv 3.10.14 bw
pyenv local bw
```

## Install pip dependencies

```bash
pip install -r requirements.txt
```
