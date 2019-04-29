# Development Environment

From the early days of [Cloudfeaster](https://www.cloudfeaster.com) it
has been important to have quick setup of a spider development environment
that produces predictable outcomes. Spider development can be challenging
enough and we don't need to add to this challenge with a long and complex
development environment setup.

Step #1: configure your development machine.
See the instructions [here](https://github.com/simonsdave/cloudfeaster/blob/master/docs/spider_authors.md#spider-development-environment) for all the details.

Step #2: Grab a copy of the git repo.

```bash
~> git pull
Enter passphrase for key '/Users/simonsdave/.ssh/id_rsa':
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
.
.
.
```

Step #3: Configue the development environment.

```bash
~> source cfg4dev
New python executable in /Users/simonsdave/gaming-spiders/env/bin/python
Installing setuptools, pip, wheel...
done.
.
.
.
```

Step #4: Run all spiders to confirm everything's working correctly.

```bash
(env) ~> run-all-spiders.sh
bigfishonlinegames.py
gamehouseonlinegames.py
gamesonly.py
hiddenobjectgames.py
mahjonggames.py
match3games.py
mindgames.py
miniclip.py
msnonlinegames.py
solitaireonline.py
(env) ~>
```
