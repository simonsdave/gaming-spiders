#!/usr/bin/env bash
#
# this script ...
#

set -e

if [ $# != 2 ]; then
    echo "usage: $(basename "$0") <username> <tag>" >&2
    exit 1
fi

USERNAME=${1:-}
TAG=${2:-latest}

echo "$USERNAME/gaming-spiders:$TAG"

exit 0
