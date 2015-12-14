#!/usr/bin/env bash

#
# this shell script is intended to be used as part of a CI build
# to run all of the spiders in this repo and exit with a non-zero
# status code of any of the spiders fail.
#

if [ "-v" == "${1:-}" ]; then
    VERBOSE=1
    shift
else
    VERBOSE=0
fi

if [ $# -ne 0 ]; then
    echo "usage: `basename $0`" >&2
    exit 1
fi

SCRIPT_DIR_NAME="$( cd "$( dirname "$0" )" && pwd )"

EXIT_CODE=0

for GAMING_SPIDER in $SCRIPT_DIR_NAME/../gaming_spiders/*.py
do
    if [ -x $GAMING_SPIDER ]; then
        echo $(python -c "import os; print os.path.basename(\"$GAMING_SPIDER\")")

        SPIDER_OUTPUT=`mktemp 2> /dev/null || mktemp -t DAS`
        $GAMING_SPIDER >& $SPIDER_OUTPUT
        if [ "$?" != "0" ]; then
            EXIT_CODE=1
            cat $SPIDER_OUTPUT
        fi
        rm $SPIDER_OUTPUT
    fi
done

exit $EXIT_CODE