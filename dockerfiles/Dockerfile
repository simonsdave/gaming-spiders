ARG CLF_VERSION
FROM simonsdave/cloudfeaster-lite:v${CLF_VERSION}

LABEL maintainer="Dave Simons"

USER root

COPY package.tar.gz /tmp/package.tar.gz
RUN pip install /tmp/package.tar.gz
RUN chmod a+x "$(python -c 'import gaming_spiders, os; print(os.path.dirname(gaming_spiders.__file__))')/"*.py
RUN chmod a-x "$(python -c 'import gaming_spiders, os; print(os.path.dirname(gaming_spiders.__file__))')/"__init__.py
RUN rm -f /tmp/package.tar.gz

USER headless
