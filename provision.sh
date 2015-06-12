#!/usr/bin/env bash
#
# This script provisions a Vagrant hosted Ubuntu 14.04 image for
# the task of creating the gaming_spiders docker image.
#

apt-get update

apt-get install -y docker.io

apt-get install -y curl
curl https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
apt-get update
apt-get install -y google-chrome-stable

apt-get install -y xvfb

apt-get install -y unzip
curl -s --output chromedriver.zip http://chromedriver.storage.googleapis.com/2.15/chromedriver_linux64.zip
unzip chromedriver.zip
rm chromedriver.zip
mv chromedriver /usr/bin/.
chown root.root /usr/bin/chromedriver
chmod a+wrx /usr/bin/chromedriver

apt-get install -y git

apt-get install -y python-virtualenv
apt-get install -y python-dev

exit 0
