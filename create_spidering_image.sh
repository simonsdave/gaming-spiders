#!/usr/bin/env bash
#
# This script ...
#

set -x

rm -rf "$(PWD)/dist"
python setup.py sdist --formats=gztar

IMAGE_VERSION=$(python - <<EOF
import gaming_spiders
print gaming_spiders.__version__
EOF
)

sudo docker kill `sudo docker ps --no-trunc -q` >& /dev/null
sudo docker rm `sudo docker ps --no-trunc -a -q` >& /dev/null

CONTAINER="simonsdave/gaming_spiders:$IMAGE_VERSION"
sudo docker rmi "$CONTAINER" >& /dev/null
sudo docker build -t "$CONTAINER" .
sudo docker push "$CONTAINER"

exit 0
