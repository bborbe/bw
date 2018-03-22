# BundleWrap Configuration

This repo contains my BundleWrap configuration. For more info about BundleWrap see: [http://bundlewrap.org/](http://BundleWrap.org/).

## Install pyenv

```bash
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
```

## Update pyenv versions

```bash
cd ~/.pyenv/plugins/python-build/../.. && git pull && cd -
```

## Install Python 3.6.4

```bash
pyenv install 3.6.4
```

## Install pyenv-virtualenv

```bash
git clone https://github.com/yyuu/pyenv-virtualenv
cd pyenv-virtualenv
sudo ./install.sh
```

## Create Bundlewrap env

```bash
pyenv virtualenv 3.6.4 bw
pyenv local bw
```

## Install pip dependencies

```bash
pip install -r requirements.txt
```
