# Development Environment

To increase predicability, it is recommended
that spider development be done on a [Vagrant](http://www.vagrantup.com/) provisioned
[VirtualBox](https://www.virtualbox.org/)
VM running [Ubuntu 16.04](http://releases.ubuntu.com/16.04/).
Below are the instructions for spinning up such a VM.

Spin up a VM using [create_dev_env.sh](create_dev_env.sh)
(instead of using ```vagrant up```).

```bash
>./create_dev_env.sh simonsdave simonsdave@gmail.com ~/.ssh/id_rsa.pub ~/.ssh/id_rsa
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Importing base box 'ubuntu/xenial64'...
.
.
.
>
```

SSH into the VM.

```bash
>vagrant ssh
Welcome to Ubuntu 16.04.4 LTS (GNU/Linux 4.4.0-119-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

7 packages can be updated.
7 updates are security updates.


~>
```

Start the ssh-agent in the background.

```bash
~> eval "$(ssh-agent -s)"
Agent pid 13350
~>
```

Add SSH private key for github to the ssh-agent

```bash
~> ssh-add ~/.ssh/id_rsa_github
Enter passphrase for /home/vagrant/.ssh/id_rsa_github:
Identity added: /home/vagrant/.ssh/id_rsa_github (/home/vagrant/.ssh/id_rsa_github)
~>
```

Clone the repo (note use of SSH)

```bash
~> git clone git@github.com:simonsdave/gaming-spiders.git
Cloning into 'gaming-spiders'...
remote: Counting objects: 503, done.
remote: Total 503 (delta 0), reused 0 (delta 0), pack-reused 503
Receiving objects: 100% (503/503), 61.52 KiB | 0 bytes/s, done.
Resolving deltas: 100% (315/315), done.
Checking connectivity... done.
~>
```

Configure the development environment.

```bash
~> cd gaming-spiders/
```

```bash
~/gaming-spiders> source cfg4dev
New python executable in env/bin/python
Installing setuptools, pip...done.
.
.
.
(env) ~/gaming-spiders>
```

Run all spiders.

```bash
(env) ~/gaming-spiders> run_all_spiders.sh
bigfishonlinegames.py
gamehouseonlinegames.py
gamesonly.py
hiddenobjectgames.py
mahjonggames.py
match3games.py
mindgames.py
miniclip.py
solitaireonline.py
(env) ~/gaming-spiders>
```
