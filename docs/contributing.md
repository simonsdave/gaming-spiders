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
```

```bash
```

```bash
```

```bash
```

```bash
```

```bash
(env) ~/gaming-spiders> cd dist/
(env) ~/gaming-spiders/dist> cp * /vagrant/.
(env) ~/gaming-spiders/dist> ls -la /vagrant/gaming_spiders*
-rw-rw-r--  1 vagrant vagrant 9329 Feb  9 15:32 gaming_spiders-1.2.0-py2-none-any.whl
-rw-rw-r--  1 vagrant vagrant 4274 Feb  9 15:32 gaming_spiders-1.2.0.tar.gz
(env) ~/gaming-spiders>
```

* on the [releases](https://github.com/simonsdave/gaming-spiders/releases)
page hit the <Draft a new release> button in the upper right corner
* fill out the release form as per the screenshot below
* main body of the form can be pulled directly from [CHANGELOG.md](../CHANGELOG.md)
* don't forget to attach to the release the ```gaming-spiders-*.whl``` and ```gaming-spiders-*.tar.gz```
copied to ```/vagrant``` in one of the above steps

![](release-form.png)
