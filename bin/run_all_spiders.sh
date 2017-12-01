#!/usr/bin/env bash

#
# this shell script is intended to be used as part of a CI build
# to run all of the spiders in this repo and exit with a non-zero
# status code of any of the spiders fail.
#

if [ $# -ne 0 ]; then
    echo "usage: $(basename "$0")" >&2
    exit 1
fi

EXIT_CODE=0

for GAMING_SPIDER_NAME in $(spiders.py | jq 'keys[]' | sed 's|"||g')
do
    echo "$GAMING_SPIDER_NAME"
    SPIDER_OUTPUT=$(mktemp 2> /dev/null || mktemp -t DAS)
    if ! spiderhost.py "$GAMING_SPIDER_NAME" >& "$SPIDER_OUTPUT"; then
        EXIT_CODE=1
        cat "$SPIDER_OUTPUT"
    fi
    rm "$SPIDER_OUTPUT"
done

exit $EXIT_CODE
