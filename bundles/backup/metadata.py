def add_backup_key(metadata):
    sshkey = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDM70gDI1cuIKu15VAEYnlWMFi3zGPf6shtQCzrHBv1nOOkfPdXlXACC4H5+MiTV5foAIA8PUaqOV9gow1w639TnWDL2DwPJ5RsT+P5g4eWszW5xQPo0zAKuvlTMB9JkDXGx1OpOE4e9n3++71yuvF/wVlqYxJwxeWXCdHf2ayx6OrTMcSMUIi+zqD494YBhKt+QJAiRrXGNU82FczJeK3iRMTtd+LUeGtnEoskcDOwhGfOXGsUGt3BMWLiDhGXp4ZvKUhNSTz5Kr9OCQT/uWam3nXciZrx1a2kVFJhd1ur81LRqxxDMGQjS29z6Vpd2vxG/P8mP3w2r7fvoqE33hpv'
    metadata.setdefault('users', {}).setdefault('root', {}).setdefault('authorized_keys', {})
    keys = metadata.get('users', {}).get('root', {}).get('authorized_keys', {})
    keys[sshkey] = {}
    return metadata
