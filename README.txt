Installation and Setup
======================

The following instructions apply to Ubuntu 8.04 Hardy Heron.
Assumption: libvalidator is installed and available.

$ mkdir ~/deploy
$ cd ~/deploy
$ git clone git://code.creativecommons.org/validator.git
$ cd validator
$ virtualenv --no-site-packages .
$ sudo easy_install Paste PylonsGenshi SQLAlchemy
$ paster serve --reload development.ini

To see the Web application running:
$ sudo apt-get install lynx
$ lynx 127.1:5000