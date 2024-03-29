# Change Log

All notable changes to this project will be documented in this file.
Format of this file follows [these](http://keepachangelog.com/) guidelines.
This project adheres to [Semantic Versioning](http://semver.org/).

## [%RELEASE_VERSION%] - [%RELEASE_DATE%]

### Added

* add CircleCI docker executor [authenticated pull](https://circleci.com/docs/2.0/private-images/)
* removed ```bigfishonlinegames.py``` since no longer seem to have browser based games:-(
* start using [CircleCI Scheduled Pipelines](https://circleci.com/docs/2.0/scheduled-pipelines)

### Changed

* cloudfeaster 0.9.30 -> 0.9.59
* added 2022 to LICENSE.md
* CircleCI setup_remote_docker version 19.03.13 -> 20.10.17

### Removed

* remove [Snyk](https://snyk.io/) from CI pipeline & docs
* remove LGTM badges from main README.md
* remove ```dev_env/.gitignore```

## [1.5.0] - [2019-07-18]

### Added

* Nothing

### Changed

* cloudfeaster 0.9.29 -> 0.9.30

### Removed

* Nothing

## [1.4.0] - [2019-07-08]

### Added

* Nothing

### Changed

* cloudfeaster 0.9.27 -> 0.9.29

### Removed

* Nothing

## [1.3.0] - [2019-06-23]

### Added

* add ```check-consistent-clf-version.sh``` to the CircelCI pipeline
* add ```check-circleci-config.sh``` to the CircelCI pipeline
* add ```run-bandit.sh``` to the CircleCI pipeline

### Changed

* cloudfeaster 0.9.10 -> 0.9.27
* flake8 3.7.5 -> 3.7.7

### Removed

* Nothing

## [1.2.0] - [2018-02-09]

### Added

* Nothing

### Changed

* ```bin/run_all_spiders.sh``` now discovers and runs spiders
  using ```spiders.py``` and ```spiderhost.py``` respectively
* ```bin/run_all_spiders.sh``` can now run spiders directly
  or inside a docker container
* cloudfeaster 0.9.7 -> 0.9.10

### Removed

* removed ```Xvfb``` from ```cfg4dev```

## [1.1.0] - [2017-11-28]

### Added

* document how to run spiders on [ECS](https://github.com/simonsdave/ecs)
* added ```bin/kill-and-rm-all-docker-containers.sh```

### Changed

* upgrade to [Cloudfeaster 0.9.7](https://github.com/simonsdave/cloudfeaster/releases/tag/v0.9.7)
* changed miniclip spider to be a bit smarter and figure out how many
  games where in the top N list rather than assuming it was always 10 games
* pep8 -> pycodestyle
* [dev-env](https://github.com/simonsdave/dev-env) v0.4.0 -> v0.5.1
* fixed ```msnonlinegames.py``` spider

### Removed

* Nothing

## [1.0.0] - [2016-08-17]

The real initial release of this project:-)

### Added

* Nothing

### Changed

* Nothing

### Removed

* Nothing

## [0.1.0] - [2016-05-04]

Beta release of this project!

### Added

* Nothing

### Changed

* Nothing

### Removed

* Nothing
