#!/usr/bin/env bash

set -euo pipefail

# update below to path to venv if different
VENV=".venv"

function missing_command { echo -e " \e[40m (missing command)\e[0m"; }
function skip_command { echo -e " \e[1;35m?\e[0m"; }
function success { echo -e " \e[1;30m✔\e[0m"; }

TEMP_DIR="$(mktemp -d)"
LAST_LOG="${TEMP_DIR}/last.log"
export LAST_LOG

function handle_exit {
  ret=$?
  if (( ret != 0 )); then
    echo -e " \e[1;31m✗\e[0m"
    if [[ -e "${LAST_LOG:-}" ]]; then less "${LAST_LOG}" 1>&2;
    else echo -e "\e[31mFailed to capture errors\e[0m"; 
    fi
  fi
  if [[ -e "${TEMP_DIR:-}" ]]; then
    rm -r "${TEMP_DIR}"
  fi
  exit $ret
}

trap handle_exit exit

# pre-commit functions

function pre_commit_black {
  echo -ne "\e[36mblack\e[0m"
  if [[ -n "${SKIP_BLACK:-}" ]]; then skip_command; return; fi
  black . >"${LAST_LOG}" 2>&1
  success
}

function pre_commit_flake {
  echo -ne "\e[36mflake8\e[0m"
  if [[ -n "${SKIP_FLAKE:-}" ]]; then skip_command; return; fi
  flake8 >"${LAST_LOG}" 2>&1
  success
}

function pre_commit_isort {
  echo -ne "\e[36misort\e[0m"
  if [[ -n "${SKIP_ISORT:-}" ]]; then skip_command; return; fi
  isort >"${LAST_LOG}" 2>&1
  success
}

function pre_commit_markdownlint {
  echo -ne "\e[36mmarkdownlint\e[0m"
  if [[ -n "${SKIP_MARKDOWN:-}" ]]; then skip_command; return; fi
  if ! command -v markdownlint >/dev/null; then missing_command; return; fi
  markdownlint ./**/*.md >"${LAST_LOG}" 2>&1
  success
}

function pre_commit_mkdocs {
  echo -ne "\e[36mmkdocs\e[0m"
  if [[ -n "${SKIP_MKDOCS:-}" ]]; then skip_command; return; fi
  if ! command -v mkdocs >/dev/null; then missing_command; return; fi
  mkdocs build >"${LAST_LOG}" 2>&1
  success
}

function pre_commit_mypy {
  echo -ne "\e[36mmypy\e[0m"
  if [[ -n "${SKIP_MYPY:-}" ]]; then skip_command; return; fi
  mypy . --pretty >"${LAST_LOG}" 2>&1
  success
}

function pre_commit_pytest {
  echo -ne "\e[36mpytest\e[0m ($(python --version))"
  if [[ -n "${SKIP_PYTEST:-}" ]]; then skip_command; return; fi
  pytest --cov >"${LAST_LOG}" 2>&1
  success
}

function pre_commit_shellcheck {
  echo -ne "\e[36mshellcheck\e[0m "
  if [[ -n "${SKIP_SHELLCHECK:-}" ]]; then skip_command; return; fi
  if ! command -v shellcheck >/dev/null; then missing_command; return; fi
  find ./* -type f -name "*.sh" -print0 | xargs -0 --no-run-if-empty shellcheck >"${LAST_LOG}" 2>&1
  success
}

function pre_commit {
  pre_commit_black
  pre_commit_isort
  pre_commit_flake
  pre_commit_mypy
  pre_commit_markdownlint
  pre_commit_mkdocs
  pre_commit_shellcheck
  pre_commit_pytest
}

if [[ -d "${VENV:-}" ]]; then
  # shellcheck disable=SC1091
  source "${VENV}/bin/activate" >/dev/null 2>&1
fi

pre_commit
