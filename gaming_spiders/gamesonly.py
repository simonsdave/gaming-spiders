#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import json
import sys

from selenium.webdriver.support.ui import WebDriverWait

from cloudfeaster import spider


class GamesonlySpider(spider.Spider):

    @classmethod
    def get_metadata(cls):
        return {
            'url': 'http://www.gamesonly.net/',
        }

    def crawl(self, browser):
        ten_seconds = 10
        web_driver_wait = WebDriverWait(browser, ten_seconds)

        data = {}

        for rank in range(1, 11):
            link_locator = '//h4[text()="Top rated games"]/../ul/li[text()="%d. "]/a' % rank
            link_element = web_driver_wait.until(lambda browser: browser.find_element_by_xpath(link_locator))
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
