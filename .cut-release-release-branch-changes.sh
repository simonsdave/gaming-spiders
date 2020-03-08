#!/usr/bin/env bash

set -e

SCRIPT_DIR_NAME="$( cd "$( dirname "$0" )" && pwd )"

if [ $# != 1 ]; then
    echo "usage: $(basename "$0") <release-branch>" >&2
    exit 1
fi

RELEASE_BRANCH=${1:-}

# requires.io
sed -i "" \
    -e \
    "s|?branch=master|?branch=$RELEASE_BRANCH|g" \
    "$SCRIPT_DIR_NAME/README.md"

# CodeFactor
sed -i '' \
    -e \
    "s|/badge/master|/badge/${RELEASE_BRANCH}|g" \
    "${REPO_ROOT_DIR}/README.md"

sed -i '' \
    -e \
    "s|/overview/master|/overview/${RELEASE_BRANCH}|g" \
    "${REPO_ROOT_DIR}/README.md"

# internal docs
sed -i "" \
    -e \
    "s|(docs|(https://github.com/simonsdave/gaming-spiders/tree/$RELEASE_BRANCH/docs|g" \
    "$SCRIPT_DIR_NAME/README.md"

exit 0
