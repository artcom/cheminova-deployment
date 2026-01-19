#!/usr/bin/env bash

set -eo pipefail

ufw allow 80/tcp
ufw reload
