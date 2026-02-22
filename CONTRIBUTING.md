# Contributing to BundleWrap Config

## Creating a New Bundle

1. **Create bundle directory:**
   ```bash
   mkdir bundles/<name>
   ```

2. **Register bundle in `groups/meta/bundles.py`** (⚠️ REQUIRED):
   - Add bundle name to the bundles list alphabetically
   - Example: `'postfix',` between `'nginx'` and `'rancher-server'`

3. **Add bundle to node config in `nodes/*.py`:**
   ```python
   'bundles': (
       '<name>',
   ),
   ```

4. **Create bundle items** in `bundles/<name>/items.py`

5. **Test locally** before committing:
   ```bash
   bw test
   ```

## Creating a New User

Add user to `nodes/*.py`:

```python
'users': {
    '<username>': { },
},
```

Add SSH key: `~/.ssh/authorized_keys.<username>`

## Pull Request Workflow

- Always create a branch from `origin/master`
- Run `make precommit` before pushing
- Create PR for review (never commit directly to master)
