#!/usr/bin/env bash

set -e

SCRIPT_DIR_NAME="$( cd "$( dirname "$0" )" && pwd )"

if [ $# != 1 ]; then
    echo "usage: $(basename "$0") <docker image name>" >&2
    exit 1
fi

DOCKER_IMAGE=${1:-}

CIRCLE_CI_EXECUTOR=$(grep 'image:' < "$(repo-root-dir.sh)/.circleci/config.yml" | \
    grep cloudfeaster-dev-env |
    sed -e 's|^.*\-[[:space:]]*image\:[[:space:]]*||g' |
    sed -e 's|[[:space:]]*$||g')

TEMP_DOCKERFILE=$(mktemp 2> /dev/null || mktemp -t DAS)
sed \
    -e "s|%CIRCLE_CI_EXECUTOR%|${CIRCLE_CI_EXECUTOR}|g" \
    < "${SCRIPT_DIR_NAME}/Dockerfile.template" \
    > "${TEMP_DOCKERFILE}"

CONTEXT_DIR=$(mktemp -d 2> /dev/null || mktemp -d -t DAS)

docker build \
    -t "${DOCKER_IMAGE}" \
    --file "${TEMP_DOCKERFILE}" \
    "${CONTEXT_DIR}"

rm -rf "${CONTEXT_DIR}"

exit 0
