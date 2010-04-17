# -*- coding: utf-8 -*-
""" The main controller of the Web application.

Copyright (C) 2008, 2009, 2010 Robert Gust‐Bardon and Creative Commons.
Originally contributed by Robert Gust‐Bardon.

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

import logging
import sys
import urllib, re

from validator.lib.base import *
from libvalidator import libvalidator

__author__ = "Robert Gust‐Bardon and Creative Commons"
__copyright__ = ("Copyright 2008, 2009, 2010 "
                 "Robert Gust‐Bardon and Creative Commons")
__credits__ = ["Robert Gust‐Bardon"]
__license__ = ("GNU Affero General Public License Version 3 "
               "or any later version")
__version__ = "0.1.0"
__maintainer__ = "Robert Gust‐Bardon"
__status__ = "Beta"

log = logging.getLogger(__name__)

class ValidationController(BaseController):

    def __init__(self):
        self.parser = libvalidator()

    def index(self):
        return render('validation.index')
    
    def about(self):
        return render('validation.about')
    
    def parseDirectInput(self):
        if not request.POST.has_key('input_direct'):
            c.error = 'No input provided.'
            return render('validation.error')
        try:
            c.result = self.parser.parse(request.POST['input_direct'])
        except:
            c.error = '%s %s' % (sys.exc_info()[0], sys.exc_info()[1])
            return render('validation.error')
        return render('validation.result')
        
    def parseOnlineDocument(self):
        reHyperlink = re.compile('^(?:data:|((ftp|gopher|https?)://))\S+$', re.IGNORECASE)
        if not request.GET.has_key('uri'):
            c.error = 'No Uniform Resource Identifier provided.'
            return render('validation.error')
        try:
            if reHyperlink.search(request.GET['uri']) is not None:
                remote = urllib.urlopen(request.GET['uri'])
                c.result = self.parser.parse(remote.read(), location=request.GET['uri'], headers=remote.info())
            else:
                raise 'Unsupported Uniform Resource Identifier.', ''
        except:
            c.error = '%s %s' % (sys.exc_info()[0], sys.exc_info()[1])
            return render('validation.error')
        return render('validation.result')
        
    def parseUploadedFile(self):
        try:
            request.POST['input_upload'].value
        except:
            c.error = 'No file uploaded.'
            return render('validation.error')
        try:
            c.result = self.parser.parse(request.POST['input_upload'].value)
        except:
            c.error = '%s %s' % (sys.exc_info()[0], sys.exc_info()[1])
            return render('validation.error')
        return render('validation.result')
