Development
===========

``validator`` and ``libvalidator`` work together as the front-end and
processing logic of the CC Validator, respectively.  As such, when
developing, you typically want to have both checked out.  These
instructions will help you prepare to work on the code.

First, create a working directory and check out both repositories:

  $ mkdir validator
  $ cd validator
  $ git clone git://code.creativecommons.org/libvalidator.git
  $ git clone git://code.creativecommons.org/validator.git

Once you have retrieved both repositories, you can build ``validator''
using the development configuration::

  $ cd validator
  $ python bootstrap.py
  $ ./bin/buildout -c develop.cfg

See the ``libvalidator'' README.txt for information on system
dependencies you may need to install.  Most Python dependencies will
be downloaded from the Python Package Index.

To run the web application, run:

  $ ./bin/paster serve --reload development.ini

Navigate to http://0:5000 in your browser to see it running.

