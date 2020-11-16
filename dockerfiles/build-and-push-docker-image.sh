#!/usr/bin/env bash

set -e

SCRIPT_DIR_NAME="$( cd "$( dirname "$0" )" && pwd )"

if [ $# != 3 ]; then
    echo "usage: $(basename "$0") <package> <image-name> <password>" >&2
    exit 1
fi

PACKAGE=${1:-}
IMAGE_NAME=${2:-}
PASSWORD=${3:-}

CONTEXT_DIR=$(mktemp -d 2> /dev/null || mktemp -d -t DAS)

cp "${PACKAGE}" "${CONTEXT_DIR}/package.tar.gz"

CLF_VERSION=$(grep cloudfeaster== "$(repo-root-dir.sh)/setup.py" | sed -e "s|^[[:space:]]*['\"]cloudfeaster==||g" | sed -e "s|['\"].*$||g")
TEMP_DOCKERFILE=$(mktemp 2> /dev/null || mktemp -t DAS)
sed \
    -e "s|%CLF_VERSION%|${CLF_VERSION}|g" \
    < "${SCRIPT_DIR_NAME}/Dockerfile.template" \
    > "${TEMP_DOCKERFILE}"

docker build \
    -t "${IMAGE_NAME}" \
    --file "${TEMP_DOCKERFILE}" \
    "${CONTEXT_DIR}"

rm -rf "${CONTEXT_DIR}"

echo "${PASSWORD}" | docker login --username="${IMAGE_NAME%/*}" --password-stdin
docker push "${IMAGE_NAME}"
docker logout

exit 0
