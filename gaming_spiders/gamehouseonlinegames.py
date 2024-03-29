#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-

import json
import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from cloudfeaster import spider


class GamehouseOnlineGamesSpider(spider.Spider):

    @classmethod
    def get_metadata(cls):
        return {
            'url': 'http://www.gamehouse.com/online-top-100-games?platform=online-games',
        }

    def crawl(self, browser):
        ten_seconds = 10
        web_driver_wait = WebDriverWait(browser, ten_seconds)

        data = {}

        for rank in range(1, 11):
            link_locator_fmt = "//li[@id='game_%d' and @class='gamebox_big']/a"
            link_locator = link_locator_fmt % rank
            link_element = web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, link_locator)))
            link = link_element.get_attribute('href')

            title_locator_fmt = (
                "//li[@id='game_%d' and @class='gamebox_big']/a"
                "/div[@class='rightside']/div[@class='gametitle']"
            )
            title_locator = title_locator_fmt % rank
            title_element = web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, title_locator)))
            title = title_element.get_text()

            data[rank] = {
                'title': title,
                'link': link,
            }

        return spider.CrawlResponseOk(data)


if __name__ == '__main__':
    crawl_args = spider.CLICrawlArgs(GamehouseOnlineGamesSpider)
    crawler = spider.SpiderCrawler(GamehouseOnlineGamesSpider)
    crawl_result = crawler.crawl(*crawl_args)
    print(json.dumps(crawl_result))
    sys.exit(1 if crawl_result.status_code else 0)
