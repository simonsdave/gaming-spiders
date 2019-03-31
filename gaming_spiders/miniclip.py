#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys

from cloudfeaster import spider


class MiniclipSpider(spider.Spider):

    @classmethod
    def get_metadata(cls):
        return {
            'url': 'http://www.miniclip.com/games/en/',
        }

    def crawl(self, browser):

        data = {}

        li_elements_locator = '//li[starts-with(@class, "counter-")]'
        li_elements = browser.find_elements_by_xpath(li_elements_locator)
        for li_element in li_elements:
            span_element_locator = './/span'
            span_element = li_element.find_element_by_xpath(span_element_locator)
            rank = span_element.get_int()

            link_element_locator = './/a'
            link_element = li_element.find_element_by_xpath(link_element_locator)
            link = link_element.get_attribute('href')
            title = link_element.get_text()
            title = title[title.find(' ') + 1:]

            data[rank] = {
                'title': title,
                'link': link,
            }

        return spider.CrawlResponseOk(data)


if __name__ == '__main__':
    crawl_args = spider.CLICrawlArgs(MiniclipSpider)
    crawler = spider.SpiderCrawler(MiniclipSpider)
    crawl_result = crawler.crawl(*crawl_args)
    print json.dumps(crawl_result)
    sys.exit(1 if crawl_result.status_code else 0)
