#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import importlib
import json
import os
import sys

from cloudfeaster.spider import SpiderDiscovery


if __name__ == "__main__":
    sd = SpiderDiscovery()
    metadata = sd.discover()
    updated_metadata = {}
    for spider_name in metadata.keys():
        spider_module_name = '.'.join(spider_name.split('.')[:-1])
        spider_module = importlib.import_module(spider_module_name)
        updated_metadata[os.path.basename(spider_module.__file__)] = metadata[spider_name]
    print(json.dumps(updated_metadata))

    sys.exit(0)
