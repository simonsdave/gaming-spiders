ARG CLF_VERSION
FROM simonsdave/cloudfeaster-lite:v${CLF_VERSION}

MAINTAINER Dave Simons

USER root

COPY package.tar.gz /tmp/package.tar.gz
RUN pip install /tmp/package.tar.gz
RUN rm -f /tmp/package.tar.gz

USER headless
