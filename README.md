# Deployment

Deployment scripts for the Cheminova [backend](https://github.com/artcom/cheminova-backend) and [frontend](https://github.com/artcom/cheminova-frontend).

## Requirements

- A UNIX-like machine to run Ansible (see [control-node-requirements](https://docs.ansible.com/projects/ansible/latest/installation_guide/intro_installation.html#control-node-requirements))
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Domain name
- Ubuntu 24.04 VPS reachable under your domain name per SSH
- S3 compatible storage for backups

## Setup

### Install Ansible

```bash
uv sync --locked
```

### Configure Host Variables

- Change variables in `inventory/hosts.yml` as described in comments, see extra information below.

### Create a Django secret key

```bash
uv run python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Passwords with Ansible Vault

Passwords are encrypted in the Ansible vault as encrypted strings stored in `hosts.yml`.

Create an encrypted variable ([Ansible docs](https://docs.ansible.com/ansible/latest/user_guide/vault.html#creating-encrypted-variables)):

```bash
uv run ansible-vault encrypt_string --stdin-name 'variable_name'
```

View/decrypt a variable (without editing):

```bash
uv run ansible localhost -m debug -a var='variable_name'
```

Or for a host-specific variable:

```bash
uv run ansible <hostname> -m debug -a var='variable_name'
```

### Object Storage Backups

The deployment expects an S3-compatible bucket to store:

- Periodic PostgreSQL database dumps (cron job executed on the host)
- Media file backups from the CMS (continuous mirror using the MinIO client container `media-backup`)

The access credentials and bucket information must be provided in the `inventory/hosts.yml` file.

## Usage

### Bootstrap

The bootstrapping playbook sets up the server with a `deployment` user and SSH keys.

```bash
uv run ansible-playbook playbook-bootstrap.yml
```

### Provision and deploy

```bash
uv run ansible-playbook playbook-provision.yml
uv run ansible-playbook playbook-deploy.yml
```

### Create CMS Super User

On the VPS

```bash
docker compose -f /home/deployment/compose/docker-compose.yml exec cms uv run manage.py createsuperuser
```

### Access Wagtail CMS UI with super user credentials

Navigate to `https://<your domain>/cms/admin/`

## Logs

### Docker container logs

Docker containers on the backend log to journald, logs can be accessed by container name (run `docker ps` to find the container name) using `journalctl`:

```bash
journalctl CONTAINER_NAME=$CONTAINER_NAME
```

Or with `docker compose`:

```bash
docker compose -f /home/deployment/compose/docker-compose.yml logs
```

### Docker images update logs

```bash
journalctl -t update-images
```
