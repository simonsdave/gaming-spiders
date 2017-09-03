#!/usr/bin/env bash

set -e

#
# python dev env
#
apt-get install -y python-virtualenv
apt-get install -y python-dev
apt-get build-dep -y python-crypto
apt-get install -y libcurl4-openssl-dev
apt-get install -y libffi-dev
apt-get build-dep -y python-pycurl
apt-get install -y unzip

#
# install latest version of chrome
#
curl https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
apt-get update
apt-get install -y google-chrome-stable

#
# install chromedriver
#
pushd /tmp
apt-get install -y unzip
CHROMEDRIVER_SOURCE=http://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip
CHROMEDRIVER_ZIP=chromedriver.zip
CHROMEDRIVER_BIN=/usr/local/bin/chromedriver
curl -s --output "$CHROMEDRIVER_ZIP" "$CHROMEDRIVER_SOURCE"
unzip "$CHROMEDRIVER_ZIP"
mv chromedriver "$CHROMEDRIVER_BIN"
chown root.root "$CHROMEDRIVER_BIN"
chmod a+x "$CHROMEDRIVER_BIN"
apt-get remove -y unzip
popd

#
# install xvfb
#
apt-get install -y xvfb

exit 0
