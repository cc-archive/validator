Installation and Setup
======================

The following instructions apply to Ubuntu 8.10 Intrepid Ibex.
Assumption: libvalidator has been installed according to the instructions.

$ git clone git://code.creativecommons.org/validator.git
$ cd validator
$ git submodule init
$ git submodule update
$ virtualenv --no-site-packages .
$ python bootstrap/bootstrap.py
$ buildout
$ buildout install
$ python setup.py bdist_egg
$ easy_install --install-dir ~/.python/lib/python2.5/site-packages \
  --prefix ~/.python dist/*

To run the Web application:
$ paster serve --reload development.ini

To see the Web application running:
$ sudo aptitude install lynx
$ lynx 127.1:5000
