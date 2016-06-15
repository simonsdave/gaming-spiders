# gaming-spiders
![Maintained](https://img.shields.io/maintenance/yes/2016.svg)
[![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT)
![Python 2.7](https://img.shields.io/badge/python-2.7-FFC100.svg?style=flat)
[![Requirements Status](https://requires.io/github/simonsdave/gaming-spiders/requirements.svg?branch=master)](https://requires.io/github/simonsdave/gaming-spiders/requirements/?branch=master)
[![Build Status](https://travis-ci.org/simonsdave/gaming-spiders.svg?branch=master)](https://travis-ci.org/simonsdave/gaming-spiders)

A collection of [Cloudfeaster](https://github.com/simonsdave/cloudfeaster)
spiders for various gaming services.

##Getting Started

```bash
>cd
>git clone https://github.com/simonsdave/gaming-spiders.git
Cloning into 'gaming-spiders'...
remote: Counting objects: 31, done.
remote: Compressing objects: 100% (25/25), done.
remote: Total 31 (delta 9), reused 13 (delta 1), pack-reused 0
Unpacking objects: 100% (31/31), done.
Checking connectivity... done.
>cd gaming-spiders/
>source cfg4dev
<<<snip lots>>>
(env)>cd gaming_spiders
(env)>./miniclip.py | jq
{
  "status": "Ok",
  "status_code": 0,
  "data": {
    "1": {
      "link": "http://www.miniclip.com/games/8-ball-pool-multiplayer/en/#t-w-t",
      "title": "8 Ball Pool"
    },
    "2": {
      "link": "http://www.miniclip.com/games/agar-io/en/#t-w-t",
      "title": "Agar.io"
    },
    "3": {
      "link": "http://www.miniclip.com/games/contract-wars/en/#t-w-t",
      "title": "Contract Wars"
    },
    "4": {
      "link": "http://www.miniclip.com/games/empire/en/#t-w-t",
      "title": "Empire"
    },
    "5": {
      "link": "http://www.miniclip.com/games/adventure-capitalist/en/#t-w-t",
      "title": "AdVenture Capitalist"
    },
    "6": {
      "link": "http://www.miniclip.com/games/game-of-thrones-ascent/en/#t-w-t",
      "title": "Game of Thrones Ascent"
    },
    "7": {
      "link": "http://www.miniclip.com/games/soccer-stars-mobile/en/#t-w-t",
      "title": "Soccer Stars Mobile"
    },
    "8": {
      "link": "http://www.miniclip.com/games/tanki-online/en/#t-w-t",
      "title": "Tanki Online"
    },
    "9": {
      "link": "http://www.miniclip.com/games/free-running-2/en/#t-w-t",
      "title": "Free Running 2"
    },
    "10": {
      "link": "http://www.miniclip.com/games/bike-rivals/en/#t-w-t",
      "title": "Bike Rivals"
    }
  }
}
(env)>
```
