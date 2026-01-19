# Check Required Variables

Ansible role that checks that required variables are defined.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values `(see defaults/main.yml)`:

```yaml
required_vars: {}
```

Set required variables to null e.g in `defaults/main.yml` otherwise the role will fail if the variable is not defined with the following error:

```bash
"Unable to look up a name or access an attribute in template string ({{ required_vars | dict2items }}).\nMake sure your variable name does not contain invalid characters like '-': dict2items requires a dictionary, got <class 'ansible.template.native_helpers.AnsibleUndefined'> instead.. dict2items requires a dictionary, got <class 'ansible.template.native_helpers.AnsibleUndefined'> instead."
```

```yaml
# defaults/main.yml
var1_name: null
var2_name: null
```

Pass the variable to check to `required_vars`:

```yaml
required_vars:
  var1_name: "{{ var1_name }}"
  var2_name: "{{ var2_name }}"
```

Add `no_log` option for `silent_vars`:

```yaml
silent_vars:
  - "var1_name"
```

## Dependencies

None.

# Example Playbook

```yaml
- name: Check required variables
  hosts: all
  become: true
  roles:
    - role: check-required-variables
      required: "some value"
      required_vars:
        required: "{{ required }}"
```

## Test

### Requirements

- python >= 3.12
- docker

### Run

```bash
pip install -r requirements.txt
molecule test --all
```

## License

MIT
