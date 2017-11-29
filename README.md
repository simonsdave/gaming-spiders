# gaming-spiders
![Maintained](https://img.shields.io/maintenance/yes/2017.svg)
[![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT)
![Python 2.7](https://img.shields.io/badge/python-2.7-FFC100.svg?style=flat)
[![Requirements Status](https://requires.io/github/simonsdave/gaming-spiders/requirements.svg?branch=release-1.1.0)](https://requires.io/github/simonsdave/gaming-spiders/requirements/?branch=release-1.1.0)
[![Build Status](https://travis-ci.org/simonsdave/gaming-spiders.svg?branch=release-1.1.0)](https://travis-ci.org/simonsdave/gaming-spiders)
[![docker-simonsdave](https://img.shields.io/badge/docker-simonsdave%2Fgaming%20spiders-blue.svg)](https://hub.docker.com/r/simonsdave/gaming-spiders/)

A collection of [Cloudfeaster](https://github.com/simonsdave/cloudfeaster)
spiders for various gaming services.

## Getting Started

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
(env)>./miniclip.py | jq .
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

## Running Spiders on [ECS](https://github.com/simonsdave/ecs) Deployment

Discover available spiders.
Steps below assume the environment variables ```ECS_ENDPOINT```, ```ECS_KEY``` and ```ECS_SECRET```
have already been set.

```bash
>cat gaming-spiders.json
{
  "docker_image": "simonsdave/gaming-spiders:latest",
  "cmd": [
    "spiders.py"
  ]
}
>curl \
   -s \
   -u $ECS_KEY:$ECS_SECRET \
   -X POST \
   -H "Content-Type: application/json" \
   --data-binary @gaming_spiders.json \
   $ECS_ENDPOINT/v1.1/tasks | \
   jq .stdout | \
   sed -e 's|"||g' | \
   base64 --decode | \
   jq .
{
 "gaming_spiders.mindgames.MindGamesSpider": {
   "url": "http://www.mindgames.com/?sort=mostPlayed",
   "factor_display_names": {},
   "ttl": 60,
   "factor_display_order": []
 },
 "gaming_spiders.gamehouseonlinegames.GamehouseOnlineGamesSpider": {
   "url": "http://www.gamehouse.com/online-top-100-games?platform=online-games",
   "factor_display_names": {},
   "ttl": 60,
   "factor_display_order": []
 },
 "gaming_spiders.hiddenobjectgames.HiddenObjectGamesSpider": {
   "url": "http://www.hiddenobjectgames.com/?sort=mostPlayed",
   "factor_display_names": {},
   "ttl": 60,
   "factor_display_order": []
 },
 "gaming_spiders.match3games.Match3GamesSpider": {
   "url": "http://www.match3games.com/?sort=mostPlayed",
   "factor_display_names": {},
   "ttl": 60,
   "factor_display_order": []
 },
 "gaming_spiders.solitaireonline.SolitaireOnlineSpider": {
   "url": "http://www.solitaireonline.com/?sort=mostPlayed",
   "factor_display_names": {},
   "ttl": 60,
   "factor_display_order": []
 },
 "gaming_spiders.gamesonly.GamesonlySpider": {
   "url": "http://www.gamesonly.net/",
   "factor_display_names": {},
   "ttl": 60,
   "factor_display_order": []
 },
 "gaming_spiders.mahjonggames.MahjongGamesSpider": {
   "url": "http://www.mahjonggames.com/?sort=mostPlayed",
   "factor_display_names": {},
   "ttl": 60,
   "factor_display_order": []
 },
 "gaming_spiders.miniclip.MiniclipSpider": {
   "url": "http://www.miniclip.com/games/en/",
   "factor_display_names": {},
   "ttl": 60,
   "factor_display_order": []
 },
 "gaming_spiders.bigfishonlinegames.BigFishOnlineGamesSpider": {
   "url": "http://www.bigfishgames.com/online-games/index.html",
   "factor_display_names": {},
   "ttl": 60,
   "factor_display_order": []
 }
}
```

Now we know what spiders are available.
Let's run the [Miniclip](http://www.miniclip.com/games/en/) spider.

```bash
>cat cat gaming_spider.json
{
  "docker_image": "simonsdave/gaming-spiders:latest",
  "cmd": [
    "spiderhost.sh",
    "gaming_spiders.miniclip.MiniclipSpider"
  ]
}
>curl \
   -s \
   -u $ECS_KEY:$ECS_SECRET \
   -X POST \
   -H "Content-Type: application/json" \
   --data-binary @gaming_spider.json \
   $ECS_ENDPOINT/v1.1/tasks | \
   jq .stdout | \
   sed -e 's|"||g' | \
   base64 --decode | \
   jq .
{
 "1": {
   "link": "http://www.miniclip.com/games/diepio/en/#t-w-t-H",
   "title": "Diep.io"
 },
 "2": {
   "link": "http://www.miniclip.com/games/8-ball-pool-multiplayer/en/#t-w-t-H",
   "title": "8 Ball Pool"
 },
 "3": {
   "link": "http://www.miniclip.com/games/slitherio/en/#t-w-t-H",
   "title": "Slither.io"
 },
 "4": {
   "link": "http://www.miniclip.com/games/tanki-online/en/#t-w-t-H",
   "title": "Tanki Online"
 },
 "5": {
   "link": "http://www.miniclip.com/games/agar-io/en/#t-w-t-H",
   "title": "Agar.io"
 },
 "6": {
   "link": "http://www.miniclip.com/games/soccer-stars-mobile/en/#t-w-t-H",
   "title": "Soccer Stars Mobile"
 },
 "7": {
   "link": "http://www.miniclip.com/games/soccer-physics/en/#t-w-t-H",
   "title": "Soccer Physics"
 },
 "8": {
   "link": "http://www.miniclip.com/games/basketball-stars/en/#t-w-t-H",
   "title": "Basketball Stars"
 },
 "9": {
   "link": "http://www.miniclip.com/games/super-soccer-noggins/en/#t-w-t-H",
   "title": "Super Soccer Noggins"
 },
 "10": {
   "link": "http://www.miniclip.com/games/color-switch/en/#t-w-t-H",
   "title": "Color Switch"
 },
 "spider": {
   "version": "ae6287c4047e9371e66ff8426b7818418b2d3de5",
   "name": "gaming_spiders.miniclip.MiniclipSpider"
 },
 "crawl_time_in_ms": 6411,
 "status": "Ok",
 "status_code": 0
}
```
