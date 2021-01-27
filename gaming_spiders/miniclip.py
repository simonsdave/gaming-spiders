#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import json
import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from cloudfeaster import spider


class MiniclipSpider(spider.Spider):

    @classmethod
    def get_metadata(cls):
        return {
            'url': 'http://www.miniclip.com/games/en/',
        }

    def crawl(self, browser):
        ten_seconds = 10
        web_driver_wait = WebDriverWait(browser, ten_seconds)

        data = {}

        xpath = '//li[starts-with(@class, "counter-")]/a'
        link_elements = web_driver_wait.until(EC.visibility_of_all_elements_located((By.XPATH, xpath)))
        for rank in range(0, min(10, len(link_elements))):
            link_element = link_elements[rank]

            link = link_element.get_attribute('href')
            title = link_element.get_text()

            data[rank + 1] = {
                'title': title,
                'link': link,
            }

        return spider.CrawlResponseOk(data)


if __name__ == '__main__':
    crawl_args = spider.CLICrawlArgs(MiniclipSpider)
    crawler = spider.SpiderCrawler(MiniclipSpider)
    crawl_result = crawler.crawl(*crawl_args)
    print(json.dumps(crawl_result))
    sys.exit(1 if crawl_result.status_code else 0)
