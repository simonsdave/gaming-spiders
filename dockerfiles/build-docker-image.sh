#!/usr/bin/env bash

set -e

SCRIPT_DIR_NAME="$( cd "$( dirname "$0" )" && pwd )"

if [ $# != 2 ]; then
    echo "usage: $(basename "$0") <package> <image-name>" >&2
    exit 1
fi

PACKAGE=${1:-}
IMAGE_NAME=${2:-}

CONTEXT_DIR=$(mktemp -d 2> /dev/null || mktemp -d -t DAS)
cp "${PACKAGE}" "${CONTEXT_DIR}/package.tar.gz"

CLF_VERSION=$(grep cloudfeaster== "$(repo-root-dir.sh)/setup.py" | sed -e "s|^[[:space:]]*['\"]cloudfeaster==||g" | sed -e "s|['\"].*$||g")

docker build \
    -t "${IMAGE_NAME}" \
    --build-arg "CLF_VERSION=${CLF_VERSION}" \
    --file "${SCRIPT_DIR_NAME}/Dockerfile" \
    "${CONTEXT_DIR}"

rm -rf "${CONTEXT_DIR}"

exit 0
