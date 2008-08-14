import logging
import sys
import urllib

from validator.lib.base import *
from libvalidator import libvalidator

log = logging.getLogger(__name__)

class ValidationController(BaseController):

    def __init__(self):
        self.parser = libvalidator()
        pass

    def index(self):
        return render('validation.index')
    
    def about(self):
        return render('validation.about')
    
    def parseDirectInput(self):
        try:
            c.result = self.parser.parse(request.POST['input_direct'])
        except:
            c.error = '%s %s' % (sys.exc_info()[0], sys.exc_info()[1])
            return render('validation.error')            
        return render('validation.result')
        
    def parseOnlineDocument(self):
        try:
            remote = urllib.urlopen(request.POST['input_remote'])
            c.result = self.parser.parse(remote.read(), location=request.POST['input_remote'], headers=remote.info())
        except:
            c.error = '%s %s' % (sys.exc_info()[0], sys.exc_info()[1])
            return render('validation.error')
        return render('validation.result')
        
    def parseUploadedFile(self):
        try:
            c.result = self.parser.parse(request.POST['input_upload'].value)
        except:
            c.error = '%s %s' % (sys.exc_info()[0], sys.exc_info()[1])
            return render('validation.error')
        return render('validation.result')
