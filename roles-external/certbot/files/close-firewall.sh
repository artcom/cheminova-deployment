#!/usr/bin/env bash

set -eo pipefail

ufw delete allow 80/tcp
ufw reload
