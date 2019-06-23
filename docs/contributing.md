# Contributing

> NOTE: these are not yet complete - they were copied from the [simonsdave / cloudfeaster](https://github.com/simonsdave/cloudfeaster)
> and still need to be edited.

The following instructions describe how you can contribute
to this project.

## Getting Started

See [this](../dev_env) for details of how to configure a development environment
and get the automated tests working.

## Branching and Versioning Strategy

* all development is done on the ```master``` branch
* we use [Semantic Versioning](http://semver.org/)
* for each release a new branch is created from master called ```release-<version>```

## How To Cut a Release

* this process leverages all the good work in from the [simonsdave / dev-env](https://github.com/simonsdave/dev-env) project
* the shell script ```cut-release.sh``` automates much of the release process
* make sure your ```~/.pypirc``` is setup

```bash
(env)>cut-release.sh
Already on 'master'
Your branch is up to date with 'origin/master'.
diff --git a/CHANGELOG.md b/CHANGELOG.md
index ad74c55..aa8fcc5 100644
--- a/CHANGELOG.md
+++ b/CHANGELOG.md
@@ -4,7 +4,7 @@ All notable changes to this project will be documented in this file.
 Format of this file follows [these](http://keepachangelog.com/) guidelines.
 This project adheres to [Semantic Versioning](http://semver.org/).

-## [%RELEASE_VERSION%] - [%RELEASE_DATE%]
+## [1.3.0] - [2019-06-23]

 ### Added

These changes to master for release look ok? (y/n)>
```

```bash
[master 1bfb392] 1.3.0 pre-release prep
 1 file changed, 1 insertion(+), 1 deletion(-)
diff --git a/CHANGELOG.md b/CHANGELOG.md
index aa8fcc5..85115c6 100644
--- a/CHANGELOG.md
+++ b/CHANGELOG.md
@@ -4,6 +4,20 @@ All notable changes to this project will be documented in this file.
 Format of this file follows [these](http://keepachangelog.com/) guidelines.
 This project adheres to [Semantic Versioning](http://semver.org/).

+## [%RELEASE_VERSION%] - [%RELEASE_DATE%]
+
+### Added
+
+* Nothing
+
+### Changed
+
+* Nothing
+
+### Removed
+
+* Nothing
+
 ## [1.3.0] - [2019-06-23]

 ### Added
diff --git a/gaming_spiders/__init__.py b/gaming_spiders/__init__.py
index 19b4f1d..96e3ce8 100644
--- a/gaming_spiders/__init__.py
+++ b/gaming_spiders/__init__.py
@@ -1 +1 @@
-__version__ = '1.3.0'
+__version__ = '1.4.0'
These changes to master for next release look ok? (y/n)>
```

```bash
[master 748fcab] Prep CHANGELOG.md for next release
 2 files changed, 15 insertions(+), 1 deletion(-)
Switched to branch 'release-1.3.0'
diff --git a/README.md b/README.md
index db5bdc7..d9d9d8b 100644
--- a/README.md
+++ b/README.md
@@ -3,7 +3,7 @@
 ![Maintained](https://img.shields.io/maintenance/yes/2019.svg)
 [![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT)
 ![Python 2.7](https://img.shields.io/badge/python-2.7-FFC100.svg?style=flat)
-[![Requirements Status](https://requires.io/github/simonsdave/gaming-spiders/requirements.svg?branch=master)](https://requires.io/github/simonsdave/gaming-spiders/requirements/?branch=master)
+[![Requirements Status](https://requires.io/github/simonsdave/gaming-spiders/requirements.svg?branch=release-1.3.0)](https://requires.io/github/simonsdave/gaming-spiders/requirements/?branch=release-1.3.0)
 [![CircleCI](https://circleci.com/gh/simonsdave/gaming-spiders.svg?style=shield)](https://circleci.com/gh/simonsdave/gaming-spiders)
 [![Vulnerabilities](https://snyk.io/test/github/simonsdave/gaming-spiders/badge.svg)](https://snyk.io/test/github/simonsdave/gaming-spiders)

@@ -81,7 +81,7 @@ Now let's run one of the spiders.
 ## What Next

 * see [this](https://github.com/simonsdave/cloudfeaster/blob/master/docs/story.md) for some background on the Cloudfeaster project
-* see [these](docs/contributing.md) instructions
+* see [these](https://github.com/simonsdave/gaming-spiders/tree/release-1.3.0/docs/contributing.md) instructions
 describe how to setup your development environment and
 start contributing to these spiders
 * [this](https://github.com/simonsdave/cloudfeaster/blob/master/docs/spider_authors.md) describes
These changes to release-1.3.0 look ok? (y/n)>
```

```bash
[release-1.3.0 acc7ad6] 1.3.0 release prep
 1 file changed, 2 insertions(+), 2 deletions(-)
All changes made locally. Ok to push changes to github? (y/n)>
```

```bash
Switched to branch 'master'
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)
Counting objects: 8, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (7/7), done.
Writing objects: 100% (8/8), 762 bytes | 762.00 KiB/s, done.
Total 8 (delta 5), reused 0 (delta 0)
remote: Resolving deltas: 100% (5/5), completed with 3 local objects.
To github.com:simonsdave/gaming-spiders.git
   099a435..748fcab  master -> master
Switched to branch 'release-1.3.0'
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 343 bytes | 343.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote:
remote: Create a pull request for 'release-1.3.0' on GitHub by visiting:
remote:      https://github.com/simonsdave/gaming-spiders/pull/new/release-1.3.0
remote:
To github.com:simonsdave/gaming-spiders.git
 * [new branch]      release-1.3.0 -> release-1.3.0
find: /Users/dave/gaming-spiders/dist: No such file or directory
Switched to branch 'master'
Your branch is up to date with 'origin/master'.
(env)>
```
