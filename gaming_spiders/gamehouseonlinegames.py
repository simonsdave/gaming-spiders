#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys

from cloudfeaster import spider

user_agent = (
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 '
    'Safari/537.36'
)


class GamehouseOnlineGamesSpider(spider.Spider):

    @classmethod
    def get_metadata(cls):
        return {
            'url': 'http://www.gamehouse.com/online-top-100-games?platform=online-games',
        }

    def crawl(self, browser):

        data = {}

        for rank in range(1, 21):
            link_locator_fmt = "//li[@id='game_%d' and @class='gamebox_big']/a"
            link_locator = link_locator_fmt % rank
            link_element = browser.find_element_by_xpath(link_locator)
            link = link_element.get_attribute("href")

            title_locator_fmt = (
                "//li[@id='game_%d' and @class='gamebox_big']/a"
                "/div[@class='rightside']/div[@class='gametitle']"
            )
            title_locator = title_locator_fmt % rank
            title_element = browser.find_element_by_xpath(title_locator)
            title = title_element.get_text()

            data[rank] = {
                "title": title,
                "link": link,
            }

        return spider.CrawlResponseOk(data)


if __name__ == "__main__":
    crawl_args = spider.CLICrawlArgs(GamehouseOnlineGamesSpider)
    crawler = spider.SpiderCrawler(GamehouseOnlineGamesSpider)
    crawl_result = crawler.crawl(*crawl_args)
    print json.dumps(crawl_result)
    sys.exit(1 if crawl_result.status_code else 0)
