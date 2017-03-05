FROM simonsdave/cloudfeaster:v0.9.4

MAINTAINER Dave Simons

RUN mkdir /tmp/spiders
COPY spiders.tar.gz /tmp/spiders/spiders.tar.gz

RUN pip install --process-dependency-links /tmp/spiders/spiders.tar.gz

RUN rm -rf /tmp/spiders
