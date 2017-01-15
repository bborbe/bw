# def enabled_groups(metadata):
#     for username, data in metadata.get('users', {}).items():
#         if data.get('enabled', False):
#             group = metadata.setdefault('groups', {}).setdefault(username, {})
#             group['enabled'] = True
#     return metadata
