# gaming-spiders

![Maintained](https://img.shields.io/maintenance/yes/2019.svg)
[![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT)
![Python 2.7](https://img.shields.io/badge/python-2.7-FFC100.svg?style=flat)
[![Requirements Status](https://requires.io/github/simonsdave/gaming-spiders/requirements.svg?branch=master)](https://requires.io/github/simonsdave/gaming-spiders/requirements/?branch=master)
[![CircleCI](https://circleci.com/gh/simonsdave/gaming-spiders.svg?style=svg)](https://circleci.com/gh/simonsdave/gaming-spiders)
[![Vulnerabilities](https://snyk.io/test/github/simonsdave/gaming-spiders/badge.svg)](https://snyk.io/test/github/simonsdave/gaming-spiders)

A collection of [Cloudfeaster](https://github.com/simonsdave/cloudfeaster)
spiders for various gaming services.

## Getting Started

First follow [these](dev_env/README.md) instructions to get your development environment setup.

Now let's run one of the spiders.

```bash
run-spider.sh miniclip | jq .
{
  "1": {
    "link": "https://www.miniclip.com/games/8-ball-pool-multiplayer/en/#t-w-t-H",
    "title": "8 Ball Pool"
  },
  "2": {
    "link": "https://www.miniclip.com/games/krunkerio/en/#t-w-t-H",
    "title": "Krunker.io"
  },
  "3": {
    "link": "https://www.miniclip.com/games/police-pursuit-2/en/#t-w-t-H",
    "title": "Police Pursuit 2"
  },
  "4": {
    "link": "https://www.miniclip.com/games/tanki-online/en/#t-w-t-H",
    "title": "Tanki Online"
  },
  "5": {
    "link": "https://www.miniclip.com/games/commando-2/en/#t-w-t-H",
    "title": "Commando 2"
  },
  "6": {
    "link": "https://www.miniclip.com/games/agar-io/en/#t-w-t-H",
    "title": "Agar.io"
  },
  "7": {
    "link": "https://www.miniclip.com/games/happy-wheels/en/#t-w-t-H",
    "title": "Happy Wheels"
  },
  "8": {
    "link": "https://www.miniclip.com/games/soccer-stars-mobile/en/#t-w-t-H",
    "title": "Soccer Stars Mobile"
  },
  "9": {
    "link": "https://www.miniclip.com/games/bubble-trouble/en/#t-w-t-H",
    "title": "Bubble Trouble"
  },
  "10": {
    "link": "https://www.miniclip.com/games/flip-master/en/#t-w-t-H",
    "title": "Flip Master"
  },
  "_metadata": {
    "status": {
      "message": "Ok",
      "code": 0
    },
    "spiderArgs": [],
    "spider": {
      "version": "sha1:de33f4ed6d1837d191f3ae605f2e127688c642b8",
      "name": "__main__.MiniclipSpider"
    },
    "crawlTime": {
      "started": "2019-04-13T13:23:29.674161+00:00",
      "durationInMs": 10396
    }
  },
  "_debug": {
    "base64ChromeDriverLog": "..."
  }
}
```

## What Next

* see [these](docs/contributing.md) instructions
describe how to setup your development environment and
start contributing to these spiders
* [this](https://github.com/simonsdave/cloudfeaster/blob/master/docs/spider_authors.md) describes
how to author spiders using Cloudfeaster
* see [this](https://github.com/simonsdave/cloudfeaster/blob/master/docs/story.md) for some background on the Cloudfeaster project
