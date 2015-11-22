#!/usr/bin/env python

import json

from cloudfeaster import spider
from cloudfeaster import webdriver_spider


class GamesonlySpider(spider.Spider):

    @classmethod
    def get_metadata(cls):
        return {
            "url": "http://www.gamesonly.net/",
        }

    def crawl(self):
        with webdriver_spider.Browser(self.url) as browser:
            return self._crawl(browser)

    def _crawl(self, browser):

        data = {}

        for rank in range(1, 11):
            locator = "//h2[text()='TOP 10 GAMES']/../ul/li/span[text()='%d']/../a" % rank
            link_element = browser.find_element_by_xpath(locator)
            link = link_element.get_attribute("href")
            title = link_element.get_text()

            data[rank] = {
                "title": title,
                "link": link,
            }

        return spider.CrawlResponseOk(data)

if __name__ == "__main__":
    crawl_args = spider.CLICrawlArgs(GamesonlySpider)
    crawler = spider.SpiderCrawler(GamesonlySpider)
    crawl_result = crawler.crawl(*crawl_args)
    print json.dumps(crawl_result)
