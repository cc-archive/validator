Developing
==========

The ``validator`` and the ``libvalidator`` work together as the front-end and
processing logic of the CC Validator, respectively.  As such, when
developing, you typically want to have both checked out.  These
instructions will help you prepare to work on the code.

The following instructions apply to the minimal installation of Ubuntu 9.10.
See <https://help.ubuntu.com/community/Installation/MinimalCD> for details.

To begin with, you need to install packages that are required by the
``libvalidator``::

  $ sudo apt-get -y install gcc git-core libxslt-dev python-dev python-librdf

Aside of these packages, the following dependencies will also be installed:
binutils gcc-4.4 libc-dev-bin libc6-dev libdigest-sha1-perl liberror-perl
libgomp1 libmysqlclient16 libpq5 libpython2.6 libraptor1 librasqal1 librdf0
libxml2-dev libxslt1-dev libxslt1.1 linux-libc-dev mysql-common patch
python2.6-dev raptor-utils redland-utils zlib1g-dev

These packages require approximately 79.7 MB (in case of the minimal
installation) and 29.0 MB (in case of the standard installation).
83 MB more will be required for the installation of the software.

It is now time to pull the source code of the ``libvalidator`` and the
``validator`` from the repositories hosted by Creative Commons::

  $ mkdir ~/deploy
  $ cd ~/deploy
  $ git clone git://code.creativecommons.org/libvalidator.git
  $ git clone git://code.creativecommons.org/validator.git

Once you have retrieved both repositories, you can build the ``validator``
using the development configuration::

  $ cd ./validator
  $ python ./bootstrap.py
  $ ./bin/buildout -c ./develop.cfg

Running
=======

To run the Web application, issue the following command in
~/deploy/validator::

  $ ./bin/paster serve --reload ./development.ini

Using
=====

To use the Web application, install a Web client, for instance::

  $ sudo apt-get install links

and direct it to <http://0:5000>::

  $ links http://0:5000
