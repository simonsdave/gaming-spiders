#!/usr/bin/env bash

#
# this shell script is intended to be used as part of a CI build
# to run all of the spiders in this repo and exit with a non-zero
# status code of any of the spiders fail.
#

DOCKER_IMAGE_NAME=""

while true
do
    case "${1,,}" in
        --image)
            shift
            DOCKER_IMAGE_NAME=${1:-}
            shift
            ;;
        *)
            break
            ;;
    esac
done

spiders() {
    if [ "$DOCKER_IMAGE_NAME" == "" ]; then
        spiders.py | jq 'keys[]' | sed 's|"||g'
    else
        docker run --rm --security-opt seccomp:unconfined "$DOCKER_IMAGE_NAME" spiders.py | jq 'keys[]' | sed 's|"||g'
    fi
}

run_spider() {
    SPIDER_NAME=${1:-}
    if [ "$DOCKER_IMAGE_NAME" == "" ]; then
        spiderhost.py "$SPIDER_NAME"
    else
        docker run --rm --security-opt seccomp:unconfined "$DOCKER_IMAGE_NAME" spiderhost.py "$SPIDER_NAME"
    fi
    return $?
}

if [ $# -ne 0 ]; then
    echo "usage: $(basename "$0") [--image <docker-image-name>]" >&2
    exit 1
fi

EXIT_CODE=0

for GAMING_SPIDER_NAME in $(spiders)
do
    echo "$GAMING_SPIDER_NAME"
    SPIDER_OUTPUT=$(mktemp 2> /dev/null || mktemp -t DAS)
    if ! run_spider "$GAMING_SPIDER_NAME" >& "$SPIDER_OUTPUT"; then
        EXIT_CODE=1
        cat "$SPIDER_OUTPUT"
    fi
    rm "$SPIDER_OUTPUT"
done

exit $EXIT_CODE
