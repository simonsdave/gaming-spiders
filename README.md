# gaming-spiders

![Maintained](https://img.shields.io/maintenance/yes/2020.svg)
[![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT)
![Python 2.7](https://img.shields.io/badge/python-2.7-FFC100.svg?style=flat)
[![Requirements Status](https://requires.io/github/simonsdave/gaming-spiders/requirements.svg?branch=master)](https://requires.io/github/simonsdave/gaming-spiders/requirements/?branch=master)
[![CodeFactor](https://www.codefactor.io/repository/github/simonsdave/gaming-spiders/badge/master)](https://www.codefactor.io/repository/github/simonsdave/gaming-spiders/master)
[![CircleCI](https://circleci.com/gh/simonsdave/gaming-spiders.svg?style=shield)](https://circleci.com/gh/simonsdave/gaming-spiders)

A collection of [Cloudfeaster](https://github.com/simonsdave/cloudfeaster)
spiders for various gaming services.

## Getting Started

First follow [these](dev_env/README.md) instructions to get your development environment setup.

Now let's run one of the spiders.

```bash
(env) ~> run-spider.sh miniclip | jq .
{
  "1": {
    "link": "https://www.miniclip.com/games/8-ball-pool-multiplayer/en/#t-w-t-H",
    "title": "8 Ball Pool"
  },
  "2": {
    "link": "https://www.miniclip.com/games/soccer-stars-mobile/en/#t-w-t-H",
    "title": "Soccer Stars Mobile"
  },
  "3": {
    "link": "https://www.miniclip.com/games/krunkerio/en/#t-w-t-H",
    "title": "Krunker.io"
  },
  "4": {
    "link": "https://www.miniclip.com/games/flip-master/en/#t-w-t-H",
    "title": "Flip Master"
  },
  "5": {
    "link": "https://www.miniclip.com/games/minecraft/en/#t-w-t-H",
    "title": "Minecraft"
  },
  "6": {
    "link": "https://www.miniclip.com/games/tanki-online/en/#t-w-t-H",
    "title": "Tanki Online"
  },
  "7": {
    "link": "https://www.miniclip.com/games/basketball-stars/en/#t-w-t-H",
    "title": "Basketball Stars"
  },
  "8": {
    "link": "https://www.miniclip.com/games/agar-io/en/#t-w-t-H",
    "title": "Agar.io"
  },
  "9": {
    "link": "https://www.miniclip.com/games/flip-diving/en/#t-w-t-H",
    "title": "Flip Diving"
  },
  "10": {
    "link": "https://www.miniclip.com/games/bubble-trouble/en/#t-w-t-H",
    "title": "Bubble Trouble"
  },
  "_metadata": {
    "status": {
      "message": "Ok",
      "code": 0
    },
    "spiderArgs": [],
    "spider": {
      "version": "sha256:608b163428a0342af7c66add6c6860721b416a5fd281d72cbabd8f4e12b362a2",
      "name": "__main__.MiniclipSpider"
    },
    "crawlTime": {
      "started": "2019-05-23T10:21:55.081224+00:00",
      "durationInMs": 19651
    }
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
