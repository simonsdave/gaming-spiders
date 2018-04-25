# for testing/debugging
#
#   docker run --rm simonsdave/gaming-spiders spiders.py | jq .
#   docker run --rm simonsdave/gaming-spiders spiders.py | jq 'keys[]' | sed 's|"||g'
#   docker run --rm --security-opt seccomp:unconfined simonsdave/gaming-spiders spiderhost.py gaming_spiders.msnonlinegames.MSNOnlineGamesSpider | jq .
#

FROM simonsdave/cloudfeaster:v0.9.13

MAINTAINER Dave Simons

ENV DEBIAN_FRONTEND noninteractive

# simonsdave/cloudfeaster:v0.9.7 sets the user to headless
# and if we don't reset back to root pip install of
# spiders.tar.gz will fail - notice @ the end of this
# file how the user is set back to headless
USER root

RUN mkdir /tmp/spiders
COPY spiders.tar.gz /tmp/spiders/spiders.tar.gz
RUN pip install --process-dependency-links /tmp/spiders/spiders.tar.gz
RUN rm -rf /tmp/spiders

USER headless

ENV DEBIAN_FRONTEND newt
