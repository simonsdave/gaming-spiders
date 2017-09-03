# Development Environment

To increase predicability, it is recommended
that spider development be done on a [Vagrant](http://www.vagrantup.com/) provisioned
[VirtualBox](https://www.virtualbox.org/)
VM running [Ubuntu 14.04](http://releases.ubuntu.com/14.04/).
Below are the instructions for spinning up such a VM.

Spin up a VM using [create_dev_env.sh](create_dev_env.sh)
(instead of using ```vagrant up```).

```bash
>./create_dev_env.sh simonsdave simonsdave@gmail.com ~/.ssh/id_rsa.pub ~/.ssh/id_rsa
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Importing base box 'trusty'...
.
.
.
```

SSH into the VM.

```bash
>vagrant ssh
Welcome to Ubuntu 14.04 LTS (GNU/Linux 3.13.0-27-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

 System information disabled due to load higher than 1.0

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

0 packages can be updated.
0 updates are security updates.


vagrant@vagrant-ubuntu-trusty-64:~$
```

Start the ssh-agent in the background.

```bash
>eval "$(ssh-agent -s)"
Agent pid 25657
>
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
vagrant@vagrant-ubuntu-trusty-64:~$ git clone git@github.com:simonsdave/gaming-spiders.git
Cloning into 'gaming-spiders'...
remote: Counting objects: 315, done.
remote: Compressing objects: 100% (19/19), done.
remote: Total 315 (delta 9), reused 0 (delta 0), pack-reused 296
Receiving objects: 100% (315/315), 40.06 KiB | 0 bytes/s, done.
Resolving deltas: 100% (187/187), done.
Checking connectivity... done.
vagrant@vagrant-ubuntu-trusty-64:~$
```

Configure the development environment.

```bash
vagrant@vagrant-ubuntu-trusty-64:~$ cd gaming-spiders
vagrant@vagrant-ubuntu-trusty-64:~/gaming-spiders$ source cfg4dev
New python executable in env/bin/python
Installing setuptools, pip...done.
.
.
.
```

Run all spiders.

```bash
(env)vagrant@vagrant-ubuntu-trusty-64:~/gaming-spiders$ run_all_spiders.sh
bigfishonlinegames.py
gamesonly.py
hiddenobjectgames.py
mahjonggames.py
match3games.py
mindgames.py
miniclip.py
msnonlinegames.py
solitaireonline.py
(env)vagrant@vagrant-ubuntu-trusty-64:~/gaming-spiders$
```
