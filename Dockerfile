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

ADD gaming_spiders gaming_spiders
ADD setup.py .
ADD MANIFEST.in .

RUN python setup.py sdist --formats=gztar

RUN pip install --process-dependency-links dist/gaming_spiders-*.*.*.tar.gz
