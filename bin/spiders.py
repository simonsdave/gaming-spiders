#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import json
import sys

from cloudfeaster.spider import SpiderDiscovery


if __name__ == "__main__":
    sd = SpiderDiscovery()
    print(json.dumps(sd.discover()))

    sys.exit(0)
