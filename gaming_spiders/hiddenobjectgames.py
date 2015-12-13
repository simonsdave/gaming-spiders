#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys

from cloudfeaster import spider

from zygomatic import ZygomaticSpider


class HiddenObjectGamesSpider(ZygomaticSpider):

    @classmethod
    def get_metadata(cls):
        return {
            "url": "http://www.hiddenobjectgames.com/?sort=mostPlayed",
        }


if __name__ == "__main__":
    crawl_args = spider.CLICrawlArgs(HiddenObjectGamesSpider)
    crawler = spider.SpiderCrawler(HiddenObjectGamesSpider)
    crawl_result = crawler.crawl(*crawl_args)
    print json.dumps(crawl_result)
    sys.exit(1 if crawl_result['status_code'] else 0)
