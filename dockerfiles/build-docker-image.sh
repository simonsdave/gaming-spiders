#!/usr/bin/env bash
#
# this script builds the repo's docker images
#

set -e

SCRIPT_DIR_NAME="$( cd "$( dirname "$0" )" && pwd )"

if [ $# != 2 ] && [ $# != 3 ]; then
    echo "usage: $(basename "$0") <spiders-tar-gz> <image-name> [<password>]" >&2
    exit 1
fi

SPIDERS_TAR_GZ=${1:-}
IMAGENAME=${2:-}
PASSWORD=${3:-}

cp "$SPIDERS_TAR_GZ" "$SCRIPT_DIR_NAME/spiders.tar.gz"
docker build -t "$IMAGENAME" "$SCRIPT_DIR_NAME"
rm "$SCRIPT_DIR_NAME/spiders.tar.gz"

if [ "$PASSWORD" != "" ]; then
    docker login --username="$USERNAME" --password="$PASSWORD"
    docker push "$IMAGENAME"
fi

exit 0
