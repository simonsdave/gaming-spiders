# gaming_spiders [![Requirements Status](https://requires.io/github/simonsdave/gaming_spiders/requirements.svg?branch=master)](https://requires.io/github/simonsdave/gaming_spiders/requirements/?branch=master) [![Build Status](https://travis-ci.org/simonsdave/gaming_spiders.svg?branch=master)](https://travis-ci.org/simonsdave/gaming_spiders) 
A collection of [CloudFeaster](https://github.com/simonsdave/clf)
spiders for various gaming services.

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
(env)>
```

##Creating a Package

```bash
pushd $(mktemp -d 2> /dev/null || mktemp -d -t DAS) > /dev/null
virtualenv env
source "$PWD/env/bin/activate"
pip install pip==1.5.6
git clone https://github.com/simonsdave/gaming_spiders.git
cd gaming_spiders/
python setup.py sdist --formats=gztar
echo $(PWD)/gaming_spiders-1.0.0.tar.gz
popd > /dev/null
```
