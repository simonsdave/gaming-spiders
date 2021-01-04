# gaming-spiders

![Maintained](https://img.shields.io/maintenance/yes/2021.svg)
[![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT)
![Python 2.7](https://img.shields.io/badge/python-2.7-FFC100.svg?style=flat)
[![Requirements Status](https://requires.io/github/simonsdave/gaming-spiders/requirements.svg?branch=master)](https://requires.io/github/simonsdave/gaming-spiders/requirements/?branch=master)
[![CodeFactor](https://www.codefactor.io/repository/github/simonsdave/gaming-spiders/badge/master)](https://www.codefactor.io/repository/github/simonsdave/gaming-spiders/overview/master)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/simonsdave/gaming-spiders.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/simonsdave/gaming-spiders/context:python)
[![CircleCI](https://circleci.com/gh/simonsdave/gaming-spiders.svg?style=shield)](https://circleci.com/gh/simonsdave/gaming-spiders)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/simonsdave/gaming-spiders.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/simonsdave/gaming-spiders/alerts/)
[![docker-simonsdave/gaming-spiders](https://img.shields.io/badge/docker-simonsdave%2Fgaming--spiders-blue.svg)](https://hub.docker.com/r/simonsdave/gaming-spiders)

A collection of [Cloudfeaster](https://github.com/simonsdave/cloudfeaster)
spiders for various gaming services.

## Getting Started

First follow [these](dev_env/README.md) instructions to get your development environment setup.

Now let's run one of the spiders.

```bash
~> run-spider.sh gamehouseonlinegames.py | jq .
{
  "1": {
    "title": "TextTwist 2",
    "link": "https://www.gamehouse.com/online-games/texttwist-2"
  },
  "2": {
    "title": "Daily Mahjong",
    "link": "https://www.gamehouse.com/online-games/daily-mahjong"
  },
  "3": {
    "title": "Bubblez!",
    "link": "https://www.gamehouse.com/online-games/bubblez!"
  },
  "4": {
    "title": "Rainforest Adventure",
    "link": "https://www.gamehouse.com/online-games/rainforest-adventure"
  },
  "5": {
    "title": "Jewel Quest",
    "link": "https://www.gamehouse.com/online-games/jewel-quest"
  },
  "6": {
    "title": "Snow Queen 2",
    "link": "https://www.gamehouse.com/online-games/snow-queen-2"
  },
  "7": {
    "title": "Rummy",
    "link": "https://www.gamehouse.com/online-games/rummy"
  },
  "8": {
    "title": "Mah Jong Medley",
    "link": "https://www.gamehouse.com/online-games/mah-jong-medley"
  },
  "9": {
    "title": "Mahjong The Endless Journey",
    "link": "https://www.gamehouse.com/online-games/mahjong-the-endless-journey"
  },
  "10": {
    "title": "Mahjongg Gardens",
    "link": "https://www.gamehouse.com/online-games/mahjongg-gardens"
  },
  "_metadata": {
    "status": {
      "code": 0,
      "message": "Ok"
    },
    "spider": {
      "name": "gamehouseonlinegames.py",
      "version": "sha256:a0717e4bef6cf41069b40efc8d6bb6941e5e899231e12d5a1af083c62b74fe1d"
    },
    "crawlArgs": [],
    "crawlTime": {
      "started": "2020-12-29T21:30:46.707601+00:00",
      "durationInMs": 3957
    }
  },
  "_debug": {
    "screenshot": "/var/folders/zc/51nmqy_93559vqw_1y526y240000gn/T/tmp.ConMqmqP/screenshot.png",
    "crawlLog": "/var/folders/zc/51nmqy_93559vqw_1y526y240000gn/T/tmp.ConMqmqP/crawl-log.txt",
    "chromeDriverLog": "/var/folders/zc/51nmqy_93559vqw_1y526y240000gn/T/tmp.ConMqmqP/chromedriver-log.txt"
  }
}
~>
```

## What Next

* see [this](https://github.com/simonsdave/cloudfeaster/blob/master/docs/story.md) for some background on the Cloudfeaster project
* see [these](docs/contributing.md) instructions
  describe how to setup your development environment and
  start contributing to these spiders
* [this](https://github.com/simonsdave/cloudfeaster/blob/master/docs/spider_authors.md) describes
  how to author spiders using Cloudfeaster
