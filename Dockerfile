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
ADD gaming_spiders /tmp/gaming_spiders/gaming_spiders
COPY setup.py /tmp/gaming_spiders/setup.py
COPY MANIFEST.in /tmp/gaming_spiders/MANIFEST.in

RUN cd /tmp/gaming_spideers; python setup.py sdist --formats=gztar

RUN pip install --process-dependency-links /tmp/gaming_spiders/dist/gaming_spiders-*.*.*.tar.gz

RUN rm -rf /tmp/gaming_spiders
