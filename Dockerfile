# to build the image
#
#   sudo docker build -t simonsdave/gaming-spiders .
#
# for testing/debugging
#
#   sudo docker run -i -t simonsdave/gaming-spiders /bin/bash
#
# to push to dockerhub
#
#   sudo docker push simonsdave/gaming-spiders
#

FROM simonsdave/cloudfeaster

MAINTAINER Dave Simons

RUN mkdir /tmp/gaming_spiders
COPY spiders.tar.gz /tmp/gaming_spiders/spiders.tar.gz

RUN pip install --process-dependency-links /tmp/gaming_spiders/spiders.tar.gz

RUN rm -rf /tmp/gaming_spiders
