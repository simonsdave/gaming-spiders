#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import json
import sys

from selenium.webdriver.support.ui import WebDriverWait

from cloudfeaster import spider


class MSNOnlineGamesSpider(spider.Spider):

    @classmethod
    def get_metadata(cls):
        return {
            'url': 'http://zone.msn.com/en-us/home',
        }

    def crawl(self, browser):
        ten_seconds = 10
        web_driver_wait = WebDriverWait(browser, ten_seconds)

        data = {}
        for rank in range(1, 6):
            locator = '//ol[@id="TopGamesInfo_Top10_Table"]/li[%d]/a' % rank
            link_element = web_driver_wait.until(lambda browser: browser.find_element_by_xpath(locator))
            link = link_element.get_attribute('href')
            title = link_element.get_text()

            data[rank] = {
                'title': title,
                'link': link,
            }

        return spider.CrawlResponseOk(data)


if __name__ == "__main__":
    crawl_args = spider.CLICrawlArgs(MSNOnlineGamesSpider)
    crawler = spider.SpiderCrawler(MSNOnlineGamesSpider)
    crawl_result = crawler.crawl(*crawl_args)
    print(json.dumps(crawl_result))
    sys.exit(1 if crawl_result.status_code else 0)
