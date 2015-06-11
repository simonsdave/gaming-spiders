#!/usr/bin/env bash
#
# This script is intended to be called by Vagrant when provisioning
# the ...
#

apt-get update

apt-get install -y docker.io

exit 0
