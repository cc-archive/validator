# -*- coding: utf-8 -*-
""" The setup script.

Copyright (C) 2008, 2009, 2010 Robert Gust‐Bardon and Creative Commons.
Originally contributed by Asheesh Laroia.

This file is a part of the License Validation Service.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

__author__ = "Robert Gust‐Bardon and Creative Commons"
__copyright__ = ("Copyright 2008, 2009, 2010 "
                 "Robert Gust‐Bardon and Creative Commons")
__credits__ = ["Asheesh Laroia", "Robert Gust‐Bardon"]
__license__ = ("GNU Affero General Public License Version 3 "
               "or any later version")
__version__ = "0.1.0"
__maintainer__ = "Robert Gust‐Bardon"
__status__ = "Beta"

README = os.path.join(os.path.dirname(__file__), "README.txt")
long_description = open(README).read()

setup(
    name="validator",
    version=__version__,
    description=("A Web application that allows its users "
                 "to obtain the information about licensed objects"),
    long_description=long_description,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Pylons",
        "Intended Audience :: End Users/Desktop",
        ("License :: OSI Approved :: "
         "GNU Affero General Public License v3"),
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Text Processing :: Markup",
        "Topic :: Utilities"
        ],
    keywords="license licence extraction validation verification checking",
    author="Robert Gust‐Bardon and Creative Commons",
    url="http://validator.creativecommons.org/",
    license=("GNU Affero General Public License Version 3 "
             "or any later version"),
    packages=find_packages(exclude=["ez_setup",]),
    install_requires=['setuptools',
                      'nose',
                      'Paste',
                      'WebHelpers<0.4',
                      'Pylons == 0.9.6.1',
                      'PylonsGenshi',
                      'SQLAlchemy',
                      'libvalidator',
                      'lxml'
                      ],
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'validator': ['i18n/*/LC_MESSAGES/*.mo']},
    entry_points="""
    [paste.app_factory]
    main = validator.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """
    )

