#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import json
import sys

from cloudfeaster import spider

from gaming_spiders.zygomatic import ZygomaticSpider


class SolitaireOnlineSpider(ZygomaticSpider):

    @classmethod
    def get_metadata(cls):
        return {
            "url": "http://www.solitaireonline.com/?sort=mostPlayed",
        }


if __name__ == "__main__":
    crawl_args = spider.CLICrawlArgs(SolitaireOnlineSpider)
    crawler = spider.SpiderCrawler(SolitaireOnlineSpider)
    crawl_result = crawler.crawl(*crawl_args)
    print(json.dumps(crawl_result))
    sys.exit(1 if crawl_result.status_code else 0)
