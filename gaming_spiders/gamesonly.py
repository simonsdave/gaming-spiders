#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import json
import sys

from cloudfeaster import spider


class GamesonlySpider(spider.Spider):

    @classmethod
    def get_metadata(cls):
        return {
            'url': 'http://www.gamesonly.net/',
        }

    def crawl(self, browser):

        data = {}

        for rank in range(1, 11):
            locator = '//h4[text()="Top rated games"]/../ul/li[text()="%d. "]/a' % rank
            link_element = browser.find_element_by_xpath(locator)
            data[rank] = {
                'title': link_element.get_text(),
                'link': link_element.get_attribute('href'),
            }

        return spider.CrawlResponseOk(data)


if __name__ == '__main__':
    crawl_args = spider.CLICrawlArgs(GamesonlySpider)
    crawler = spider.SpiderCrawler(GamesonlySpider)
    crawl_result = crawler.crawl(*crawl_args)
    print(json.dumps(crawl_result))
    sys.exit(1 if crawl_result.status_code else 0)
