#!/usr/bin/env bash

set -euo pipefail

GITROOT="$(builtin cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." &>/dev/null && builtin pwd)"
SNIRK_VENV="${SNIRK_VENV:-.venv/snirk}"

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

TEMP_DIR="$(mktemp -d)"

function handle_exit {
  ret=$?
  if [[ -e "${TEMP_DIR:-}" ]]; then
    rm -rf "${TEMP_DIR}"
  fi
  exit $ret
}

trap handle_exit exit

# checkout SNI repo
commit="$(cat "${GITROOT}/snirk/sni/version.txt")"
echo "Cloning SNI..."
git clone -q https://github.com/alttpo/sni.git "${TEMP_DIR}" >/dev/null 2>&1
cd "${TEMP_DIR}" || (echo "Failed to checkout SNI" && exit 1)
echo "Checking out SNI at commit: $commit"
git checkout -q "$commit" >/dev/null 2>&1

# create python files from proto
cd "$GITROOT" || exit 1
echo "Creating python files from SNI protobuf..."
python -m grpc_tools.protoc -I "${TEMP_DIR}/protos" \
  --python_out=snirk/ --pyi_out=snirk/ --grpc_python_out=snirk/ \
  "${TEMP_DIR}/protos/sni/sni.proto" >/dev/null 2>&1

echo "Patching generated python files..."

# remove annotations on None
sed -e "/None: .*/d" snirk/sni/sni_pb2.pyi > "${TEMP_DIR}/sed.pyi"
mv "${TEMP_DIR}/sed.pyi" snirk/sni/sni_pb2.pyi

# fix "== False" to use "is"
sed -e "s/== False/is False/" snirk/sni/sni_pb2.py > "${TEMP_DIR}/sed.py"
mv "${TEMP_DIR}/sed.py" snirk/sni/sni_pb2.py

# update import path
sed -e "s/from sni import/from snirk.sni import/" snirk/sni/sni_pb2_grpc.py > "${TEMP_DIR}/sed.py"
mv "${TEMP_DIR}/sed.py" snirk/sni/sni_pb2_grpc.py

echo "Formatting generated python files..."
black snirk/sni --preview --enable-unstable-feature string_processing
isort snirk/sni/
