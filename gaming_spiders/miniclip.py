#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys

from cloudfeaster import spider
from cloudfeaster import webdriver_spider


class MiniclipSpider(spider.Spider):

    @classmethod
    def get_metadata(cls):
        return {
            "url": "http://www.miniclip.com/games/en/",
        }

    def crawl(self):
        with webdriver_spider.Browser(self.url) as browser:
            return self._crawl(browser)

    def _crawl(self, browser):

        data = {}

        link_elements_locator = "//li[starts-with(@class, 'counter-')]/a"
        link_elements = browser.find_elements_by_xpath(link_elements_locator)
        for link_element in link_elements:
            rank_element_locator = '../span'
            rank_element = link_element.find_element_by_xpath(rank_element_locator)
            rank = rank_element.get_int()
            link = link_element.get_attribute("href")
            title = link_element.get_text()

            data[rank] = {
                "title": title,
                "link": link,
            }

        return spider.CrawlResponseOk(data)


if __name__ == "__main__":
    crawl_args = spider.CLICrawlArgs(MiniclipSpider)
    crawler = spider.SpiderCrawler(MiniclipSpider)
    crawl_result = crawler.crawl(*crawl_args)
    print json.dumps(crawl_result)
    sys.exit(1 if crawl_result['_status_code'] else 0)
