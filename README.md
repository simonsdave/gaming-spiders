# gaming-spiders

![Maintained](https://img.shields.io/maintenance/yes/2020.svg)
[![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT)
![Python 2.7](https://img.shields.io/badge/python-2.7-FFC100.svg?style=flat)
[![Requirements Status](https://requires.io/github/simonsdave/gaming-spiders/requirements.svg?branch=master)](https://requires.io/github/simonsdave/gaming-spiders/requirements/?branch=master)
[![CodeFactor](https://www.codefactor.io/repository/github/simonsdave/gaming-spiders/badge/master)](https://www.codefactor.io/repository/github/simonsdave/gaming-spiders/overview/master)
[![CircleCI](https://circleci.com/gh/simonsdave/gaming-spiders.svg?style=shield)](https://circleci.com/gh/simonsdave/gaming-spiders)

A collection of [Cloudfeaster](https://github.com/simonsdave/cloudfeaster)
spiders for various gaming services.

## Getting Started

First follow [these](dev_env/README.md) instructions to get your development environment setup.

Now let's run one of the spiders.

```bash
(env) ~> run-spider.sh bigfishonlinegames.py | jq .
{
  "1": {
    "title": "Hidden Express",
    "link": "https://www.bigfishgames.com/online-games/25540/en_hidden-express/index.html"
  },
  "2": {
    "title": "Cubis Gold 2",
    "link": "https://www.bigfishgames.com/online-games/1909/en_cubis-gold-2/index.html"
  },
  "3": {
    "title": "Fitz!",
    "link": "https://www.bigfishgames.com/online-games/2222/en_fitz/index.html"
  },
  "4": {
    "title": "Bubblez!",
    "link": "https://www.bigfishgames.com/online-games/2196/en_bubblez/index.html"
  },
  "5": {
    "title": "Algerian Patience Solitaire",
    "link": "https://www.bigfishgames.com/online-games/3887/en_algerian-patience-solitaire/index.html"
  },
  "6": {
    "title": "Dreamfields",
    "link": "https://www.bigfishgames.com/online-games/25550/en_dreamfields-free-to-play/index.html"
  },
  "7": {
    "title": "The Rise of Atlantis",
    "link": "https://www.bigfishgames.com/online-games/1889/en_riseofatlantis/index.html"
  },
  "8": {
    "title": "Dragon Mahjong",
    "link": "https://www.bigfishgames.com/online-games/21826/en_dragon-mahjong/index.html"
  },
  "9": {
    "title": "Shanghai",
    "link": "https://www.bigfishgames.com/online-games/8031/en_shanghai/index.html"
  },
  "_metadata": {
    "status": {
      "code": 0,
      "message": "Ok"
    },
    "spider": {
      "name": "__main__.BigFishOnlineGamesSpider",
      "version": "sha256:44336fe0596a789d429c1840f69823c11803887fe804763b66f1ab7e12aaf95e"
    },
    "crawlArgs": [],
    "crawlTime": {
      "started": "2020-03-08T20:41:17.424941+00:00",
      "durationInMs": 4219
    }
  },
  "_debug": {
    "screenshot": "/var/folders/7x/rr443kj575s8zz54jrbrp4jc0000gn/T/tmp.JYTivkpU/screenshot.png",
    "crawlLog": "/var/folders/7x/rr443kj575s8zz54jrbrp4jc0000gn/T/tmp.JYTivkpU/crawl-log.txt",
    "chromeDriverLog": "/var/folders/7x/rr443kj575s8zz54jrbrp4jc0000gn/T/tmp.JYTivkpU/chromedriver-log.txt"
  }
}
(env) ~>
```

## What Next

* see [this](https://github.com/simonsdave/cloudfeaster/blob/master/docs/story.md) for some background on the Cloudfeaster project
* see [these](docs/contributing.md) instructions
  describe how to setup your development environment and
  start contributing to these spiders
* [this](https://github.com/simonsdave/cloudfeaster/blob/master/docs/spider_authors.md) describes
  how to author spiders using Cloudfeaster
