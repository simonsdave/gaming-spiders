ARG CLF_VERSION
FROM simonsdave/cloudfeaster-lite:latest

MAINTAINER Dave Simons

USER root

COPY package.tar.gz /tmp/package.tar.gz
RUN pip install /tmp/package.tar.gz
RUN rm -f /tmp/package.tar.gz

USER headless
