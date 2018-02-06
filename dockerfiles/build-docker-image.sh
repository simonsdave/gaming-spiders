#!/usr/bin/env bash
#
# this script builds the repo's docker images
#

set -e

SCRIPT_DIR_NAME="$( cd "$( dirname "$0" )" && pwd )"

if [ $# != 2 ]; then
    echo "usage: $(basename "$0") <spiders-tar-gz> <image-name>" >&2
    exit 1
fi

SPIDERS_TAR_GZ=${1:-}
IMAGE_NAME=${2:-}

cp "$SPIDERS_TAR_GZ" "$SCRIPT_DIR_NAME/spiders.tar.gz"
docker build -t "$IMAGE_NAME" "$SCRIPT_DIR_NAME"
rm "$SCRIPT_DIR_NAME/spiders.tar.gz"

exit 0
