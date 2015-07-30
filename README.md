#gaming_spiders
[![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT) ![Python 2.7](https://img.shields.io/badge/python-2.7-FFC100.svg?style=flat) [![Requirements Status](https://requires.io/github/simonsdave/gaming_spiders/requirements.svg?branch=master)](https://requires.io/github/simonsdave/gaming_spiders/requirements/?branch=master) [![Build Status](https://travis-ci.org/simonsdave/gaming_spiders.svg?branch=master)](https://travis-ci.org/simonsdave/gaming_spiders) [![Code Health](https://landscape.io/github/simonsdave/gaming_spiders/master/landscape.svg?style=flat)](https://landscape.io/github/simonsdave/gaming_spiders/master)

A collection of [CloudFeaster](https://github.com/simonsdave/clf)
spiders for various gaming services.

This repo leverages [DockerHub's](https://hub.docker.com/)
[automated build](https://docs.docker.com/docker-hub/builds/) feature to
keep the [simonsdave / gaming-spiders](https://registry.hub.docker.com/u/simonsdave/gaming-spiders/)
docker image up to date.

##Getting Started

```bash
>cd
>git clone https://github.com/simonsdave/gaming_spiders.git
Cloning into 'gaming_spiders'...
remote: Counting objects: 31, done.
remote: Compressing objects: 100% (25/25), done.
remote: Total 31 (delta 9), reused 13 (delta 1), pack-reused 0
Unpacking objects: 100% (31/31), done.
Checking connectivity... done.
>cd gaming_spiders/
>source cfg4dev
<<<snip lots>>>
(env)> cd gaming_spiders
(env)> ./miniclip.py
{"status": "Ok", "status_code": 0, "data": {"1": {"link": "http://www.miniclip.com/games/8-ball-pool-multiplayer/en/#t-w-t", "title": "8 Ball Pool"}, "2": {"link": "http://www.miniclip.com/games/tanki-online/en/#t-w-t", "title": "Tanki Online"}, "3": {"link": "http://www.miniclip.com/games/agar/en/#t-w-t", "title": "agar.io"}, "4": {"link": "http://www.miniclip.com/games/soccer-stars-mobile/en/#t-w-t", "title": "Soccer Stars Mobile"}, "5": {"link": "http://www.miniclip.com/games/soccer-physics/en/#t-w-t-H", "title": "Soccer Physics"}, "6": {"link": "http://www.miniclip.com/games/free-running-2/en/#t-w-t-H", "title": "Free Running 2"}, "7": {"link": "http://www.miniclip.com/games/clicker-heroes/en/#t-w-t-H", "title": "Clicker Heroes"}, "8": {"link": "http://www.miniclip.com/games/bike-rivals/en/#t-w-t-H", "title": "Bike Rivals"}, "9": {"link": "http://www.miniclip.com/games/wrestle-jump/en/#t-w-t-H", "title": "Wrestle Jump"}, "10": {"link": "http://www.miniclip.com/games/beast-quest/en/#t-w-t-H", "title": "Beast Quest"}}}
(env)>
```
