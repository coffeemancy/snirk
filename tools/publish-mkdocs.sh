#!/usr/bin/env bash

# Script to publish mkdocs to Github Pages.
#
# Based on:
#   https://github.com/mhausenblas/mkdocs-deploy-gh-pages/blob/master/action.sh

set -euo pipefail

SNIRK_VENV="${SNIRK_VENV:-.venv}"

# make sure not being run as root or with "sudo"
if (( EUID == 0 )); then
  echo "Do not run this script as root/sudo."
  exit 1
fi

# try to activate snirk virtualenv, if not running in a venv
if [[ -z "${VIRTUAL_ENV:-}" ]]; then
  if [[ -n "${SNIRK_VENV}" ]] && [[ -d "${SNIRK_VENV}" ]]; then
    echo "Activating venv: ${SNIRK_VENV}"
    # shellcheck disable=SC1091
    source "${SNIRK_VENV}/bin/activate" || (echo "Failed to activate venv: ${SNIRK_VENV}" && exit 1)
  else
    echo "Not running in virtualenv and ${SNIRK_VENV} does not exist!"
    exit 1
  fi
fi

if [[ -n "${GITHUB_TOKEN:-}" ]]; then
  echo "Using GITHUB_TOKEN..."
  remote_repo="https://x-access-token:${GITHUB_TOKEN}@github.com/coffeemancy/snirk.git"
else
  remote_repo="$(git remote get-url origin)"
fi

# create a new remote "mkdocspush", if doesn't exist
if ! git remote | grep mkdocspush; then
  if [ -z "${remote_repo}" ]; then
    echo "Could not determine remote repo to use!"
    exit 1
  fi
  echo "Adding mkdocspush remote..."
  git remote add mkdocspush "${remote_repo}"
fi

echo "Publishing mkdocs..."
mkdocs gh-deploy --force --clean --verbose --remote-name mkdocspush
