#!/usr/bin/env bash

set -e

SCRIPT_DIR_NAME="$( cd "$( dirname "$0" )" && pwd )"

if [ $# != 1 ]; then
    echo "usage: $(basename "$0") <docker image name>" >&2
    exit 1
fi

DOCKER_IMAGE=${1:-}

TEMP_DOCKERFILE=$(mktemp 2> /dev/null || mktemp -t DAS)
cp "${SCRIPT_DIR_NAME}/Dockerfile.template" "${TEMP_DOCKERFILE}"

CLF_VERSION=$(grep cloudfeaster== "${SCRIPT_DIR_NAME}/../setup.py" | sed -e "s|^[[:space:]]*['\"]cloudfeaster==||g" | sed -e "s|['\"].*$||g")
sed \
    -i '' \
    -e "s|%CLF_VERSION%|v${CLF_VERSION}|g" \
    "${TEMP_DOCKERFILE}"

CONTEXT_DIR=$(mktemp -d 2> /dev/null || mktemp -d -t DAS)

docker build \
    -t "${DOCKER_IMAGE}" \
    --file "${TEMP_DOCKERFILE}" \
    "${CONTEXT_DIR}"

rm -rf "${CONTEXT_DIR}"

exit 0
