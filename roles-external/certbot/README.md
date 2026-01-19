# Certbot

Ansible role to install and configure certbot.

# Requirements

- [check-required-variables](https://github.com/artcom/ansible-role-check-required-variables)

## Role Variables

Available variables are listed below, along with default values `(see defaults/main.yml)`:

```yaml
certbot_challenge: http
certbot_hostname: null # required when certbot_generate_standalone_cert == true
certbot_email: null # required when certbot_generate_standalone_cert == true
certbot_user: null
certbot_config_dir: /srv/config/certbot
certbot_dns_challenge_credentials: null # path to local credentials file for dns challenge
certbot_generate_standalone_cert: true
```

Required variables (role will fail if the variables are not set):

```yaml
certbot_user: null
```
