#!/usr/bin/env bash
#
# this script builds the repo's docker images
#

SCRIPT_DIR_NAME="$( cd "$( dirname "$0" )" && pwd )"

if [ "-v" == "${1:-}" ]; then
    VERBOSE=1
    shift
else
    VERBOSE=0
fi

if [ $# != 4 ]; then
    echo "usage: `basename $0` [-v] <email> <username> <password> <spiders-tar-gz>" >&2
    exit 1
fi

EMAIL=${1:-}
USERNAME=${2:-}
PASSWORD=${3:-}
SOURCE_SPIDERS_TAR_GZ=${4:-}

#
# login to dockerhub
#
docker login --email="$EMAIL" --username="$USERNAME" --password="$PASSWORD"

#
# build services image
#
cp "$SOURCE_SPIDERS_TAR_GZ" "$SCRIPT_DIR_NAME/spiders.tar.gz"
IMAGENAME=$USERNAME/gaming-spiders
docker build -t $IMAGENAME "$SCRIPT_DIR_NAME"
rm "$SCRIPT_DIR_NAME/spiders.tar.gz"
docker push $IMAGENAME

exit 0
