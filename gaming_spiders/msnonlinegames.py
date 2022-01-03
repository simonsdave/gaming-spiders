#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-

import json
import sys
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from cloudfeaster import spider


_remove_leading_rank_reg_ex = re.compile(
    r'^\d+\.\s*',
    re.IGNORECASE)


class MSNOnlineGamesSpider(spider.Spider):

    @classmethod
    def get_metadata(cls):
        return {
            'url': 'http://zone.msn.com/en-us/home',
        }

    """
    # for future use
    works_to_get_all_categories_xpath = '//div[contains(@class, "top-free-games")]/div/h3[@class="text"]'
    """

    def crawl(self, browser):
        ten_seconds = 10
        web_driver_wait = WebDriverWait(browser, ten_seconds)

        games = []

        category = 'Top FREE Games'

        xpath_fmt = (
            '//div[contains(@class, "top-free-games")]/div/h3[text()="{category}"]/'
            '../../'
            'div[@class="games"]/div[contains(@class, "game")]/a'
        )
        xpath = xpath_fmt.format(category=category)
        game_link_elements = web_driver_wait.until(EC.visibility_of_all_elements_located((By.XPATH, xpath)))
        for game_link_element in game_link_elements:
            link = game_link_element.get_attribute('href')
            title_with_leading_rank = game_link_element.get_text()
            title = _remove_leading_rank_reg_ex.sub('', title_with_leading_rank)
            games.append({
                'title': title,
                'link': link,
            })

        return spider.CrawlResponseOk({'games': games})


if __name__ == "__main__":
    crawl_args = spider.CLICrawlArgs(MSNOnlineGamesSpider)
    crawler = spider.SpiderCrawler(MSNOnlineGamesSpider)
    crawl_result = crawler.crawl(*crawl_args)
    print(json.dumps(crawl_result))
    sys.exit(1 if crawl_result.status_code else 0)
