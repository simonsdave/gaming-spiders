# gaming-spiders
![Maintained](https://img.shields.io/maintenance/yes/2018.svg)
[![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT)
![Python 2.7](https://img.shields.io/badge/python-2.7-FFC100.svg?style=flat)
[![Requirements Status](https://requires.io/github/simonsdave/gaming-spiders/requirements.svg?branch=master)](https://requires.io/github/simonsdave/gaming-spiders/requirements/?branch=master)
[![Build Status](https://travis-ci.org/simonsdave/gaming-spiders.svg?branch=master)](https://travis-ci.org/simonsdave/gaming-spiders)
[![docker-simonsdave](https://img.shields.io/badge/docker-simonsdave%2Fgaming%20spiders-blue.svg)](https://hub.docker.com/r/simonsdave/gaming-spiders/)

A collection of [Cloudfeaster](https://github.com/simonsdave/cloudfeaster)
spiders for various gaming services.

## Getting Started

First follow [these](dev_env/README.md) instructions to get your development environment setup.

Now let's run one of the spiders.

```bash
(env) ~/gaming-spiders> cd gaming_spiders
(env) ~/gaming-spiders/gaming_spiders> ./miniclip.py | jq .
{
  "1": {
    "link": "https://www.miniclip.com/games/8-ball-pool-multiplayer/en/#t-w-t-H",
    "title": "8 Ball Pool"
  },
  "2": {
    "link": "https://www.miniclip.com/games/agar-io/en/#t-w-t-H",
    "title": "Agar.io"
  },
  "3": {
    "link": "https://www.miniclip.com/games/tanki-online/en/#t-w-t-H",
    "title": "Tanki Online"
  },
  "4": {
    "link": "https://www.miniclip.com/games/diepio/en/#t-w-t-H",
    "title": "Diep.io"
  },
  "5": {
    "link": "https://www.miniclip.com/games/brutesio/en/#t-w-t-H",
    "title": "Brutes.io"
  },
  "6": {
    "link": "https://www.miniclip.com/games/soccer-stars-mobile/en/#t-w-t-H",
    "title": "Soccer Stars Mobile"
  },
  "7": {
    "link": "https://www.miniclip.com/games/flip-master/en/#t-w-t-H",
    "title": "Flip Master"
  },
  "8": {
    "link": "https://www.miniclip.com/games/bubble-trouble/en/#t-w-t-H",
    "title": "Bubble Trouble"
  },
  "9": {
    "link": "https://www.miniclip.com/games/happy-wheels/en/#t-w-t-H",
    "title": "Happy Wheels"
  },
  "10": {
    "link": "https://www.miniclip.com/games/empire/en/#t-w-t-H",
    "title": "Empire"
  },
  "_crawl_time": "2018-02-05T20:24:20.683306+00:00",
  "_status_code": 0,
  "_spider": {
    "version": "sha1:aaa69d021a88990ed1404119a699d76c55cf42d3",
    "name": "__main__.MiniclipSpider"
  },
  "_status": "Ok",
  "_crawl_time_in_ms": 11218
}
(env) ~/gaming-spiders/gaming_spiders>
```

## What Next

* see [these](docs/contributing.md) instructions
describe how to setup your development environment and
start contributing to these spiders
* [this](https://github.com/simonsdave/cloudfeaster/blob/master/docs/spider_authors.md) describes
how to author spiders using Cloudfeaster
* see [this](https://github.com/simonsdave/cloudfeaster/blob/master/docs/story.md) for some background on the Cloudfeaster project
