Installation and Setup
======================

The following instructions apply to Ubuntu 8.04 Hardy Heron.
Assumption: libvalidator is installed and available.

$ sudo apt-get install python-setuptools python-zopeinterface
$ sudo easy_install zc.buildout virtualenv
$ mkdir ~/deploy
$ cd ~/deploy
$ git clone git://code.creativecommons.org/validator.git
$ cd validator
$ virtualenv --no-site-packages .
$ git submodule init
$ git submodule update
$ python bootstrap/bootstrap.py
$ buildout
$ buildout install
$ python setup.py bdist_egg
$ paster serve --reload development.ini

To see the Web application running:
$ sudo apt-get install lynx
$ lynx 127.1:5000