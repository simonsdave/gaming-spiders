#!/usr/bin/env python

import json

from cloudfeaster import spider
from cloudfeaster import webdriver_spider


class MahjongGamesSpider(spider.Spider):

    @classmethod
    def get_metadata(cls):
        return {
            "url": "http://www.mahjonggames.com/?sort=mostPlayed",
        }

    def crawl(self):
        with webdriver_spider.Browser(self.url) as browser:
            return self._crawl(browser)

    def _crawl(self, browser):

        data = {}

        for rank in range(1, 11):
            link_locator = "//div[@class='index block-group']/div[%d]/a" % rank
            link_element = browser.find_element_by_xpath(link_locator)
            link = link_element.get_attribute("href")

            title_locator = "//div[@class='index block-group']/div[%d]/a/div/h3" % rank
            title_element = browser.find_element_by_xpath(title_locator)
            title = link_element.get_text()

            data[rank] = {
                "title": title,
                "link": link,
            }

        return spider.CrawlResponseOk(data)

if __name__ == "__main__":
    crawl_args = spider.CLICrawlArgs(MahjongGamesSpider)
    crawler = spider.SpiderCrawler(MahjongGamesSpider)
    crawl_result = crawler.crawl(*crawl_args)
    print json.dumps(crawl_result)
