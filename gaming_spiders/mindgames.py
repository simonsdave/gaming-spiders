#!/usr/bin/env python

import json

from cloudfeaster import spider

from zygomatic import ZygomaticSpider


class MindGamesSpider(ZygomaticSpider):

    @classmethod
    def get_metadata(cls):
        return {
            "url": "http://www.mindgames.com/?sort=mostPlayed",
        }


if __name__ == "__main__":
    crawl_args = spider.CLICrawlArgs(MindGamesSpider)
    crawler = spider.SpiderCrawler(MindGamesSpider)
    crawl_result = crawler.crawl(*crawl_args)
    print json.dumps(crawl_result)
