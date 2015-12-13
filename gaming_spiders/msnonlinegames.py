#!/usr/bin/env python

import json
import sys

from cloudfeaster import spider
from cloudfeaster import webdriver_spider


class MSNOnlineGamesSpider(spider.Spider):

    @classmethod
    def get_metadata(cls):
        return {
            'url': 'http://zone.msn.com/en-us/home',
        }

    def crawl(self):
        with webdriver_spider.Browser(self.url) as browser:
            return self._crawl(browser)

    def _crawl(self, browser):

        data = {}
        for rank in range(1, 6):
            locator_fmt = "//td[@class='ModulePositionCell' and text()='%d.']/../td/a"
            locator = locator_fmt % rank
            link_element = browser.find_element_by_xpath(locator)
            link = link_element.get_attribute("href")
            title = link_element.get_text()

            data[rank] = {
                "title": title,
                "link": link,
            }

        return spider.CrawlResponseOk(data)

if __name__ == "__main__":
    crawl_args = spider.CLICrawlArgs(MSNOnlineGamesSpider)
    crawler = spider.SpiderCrawler(MSNOnlineGamesSpider)
    crawl_result = crawler.crawl(*crawl_args)
    print json.dumps(crawl_result)
    sys.exit(1 if crawl_result['status_code'] else 0)
