FROM simonsdave/cloudfeaster:v0.7.0

MAINTAINER Dave Simons

RUN mkdir /tmp/spiders
COPY spiders.tar.gz /tmp/spiders/spiders.tar.gz

RUN pip install --process-dependency-links /tmp/spiders/spiders.tar.gz

RUN rm -rf /tmp/spiders
