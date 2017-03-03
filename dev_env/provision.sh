#!/usr/bin/env bash

set -e

apt-get update -y

apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" | tee /etc/apt/sources.list.d/docker.list
apt-get update
apt-get install -y docker-engine
usermod -aG docker vagrant
service docker restart

apt-get install -y git

apt-get install -y python-virtualenv
apt-get install -y python-dev
apt-get build-dep -y python-crypto
apt-get install -y libcurl4-openssl-dev
apt-get install -y libffi-dev
apt-get build-dep -y python-pycurl
apt-get install -y unzip

timedatectl set-timezone EST

curl -s -L --output /etc/jq 'https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64'
chown root.root /etc/jq
chmod a+x /etc/jq

curl https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
apt-get update
apt-get install -y google-chrome-stable

curl -s --output chromedriver.zip http://chromedriver.storage.googleapis.com/2.22/chromedriver_linux64.zip
unzip chromedriver.zip
rm chromedriver.zip
mv chromedriver /usr/bin/.
chown root.root /usr/bin/chromedriver
chmod a+wrx /usr/bin/chromedriver

apt-get install -y xvfb

DOTVIMRC=~vagrant/.vimrc

echo 'set ruler' > $DOTVIMRC
echo 'set hlsearch' >> $DOTVIMRC
echo 'filetype plugin on' >> $DOTVIMRC
echo 'set ts=4' >> $DOTVIMRC
echo 'set sw=4' >> $DOTVIMRC
echo 'set expandtab' >> $DOTVIMRC
echo 'set encoding=UTF8' >> $DOTVIMRC
echo 'syntax on' >> $DOTVIMRC
echo 'au BufNewFile,BufRead *.raml set filetype=raml' >> $DOTVIMRC
echo 'au BufNewFile,BufRead *.json set filetype=json' >> $DOTVIMRC
echo 'au BufNewFile,BufRead *.yaml set filetype=yaml' >> $DOTVIMRC
echo 'autocmd Filetype shell setlocal expandtab tabstop=4 shiftwidth=4' >> $DOTVIMRC
echo 'autocmd Filetype python setlocal expandtab tabstop=4 shiftwidth=4' >> $DOTVIMRC
echo 'autocmd FileType raml setlocal expandtab tabstop=2 shiftwidth=2' >> $DOTVIMRC
echo 'autocmd FileType yaml setlocal expandtab tabstop=2 shiftwidth=2' >> $DOTVIMRC

chown vagrant:vagrant $DOTVIMRC

echo 'export VISUAL=vim' >> ~vagrant/.profile
echo 'export EDITOR="$VISUAL"' >> ~vagrant/.profile

if [ $# == 2 ]; then
    su - vagrant -c "git config --global user.name \"${1:-}\""
    su - vagrant -c "git config --global user.email \"${2:-}\""
fi

exit 0
