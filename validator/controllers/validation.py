import logging
import sys
import urllib, re

from validator.lib.base import *
from libvalidator import libvalidator

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
