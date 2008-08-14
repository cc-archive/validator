import logging
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
    
    def parseDirectInput(self):
        try:
            c.result = self.parser.parse(request.POST['input_direct'])
        except:
            return render('validation.error')            
        return render('validation.result')
        
    def parseOnlineDocument(self):
        try:
            remote = urllib.urlopen(request.POST['input_remote'])
            c.result = self.parser.parse(remote.read(), location=request.POST['input_remote'], headers=remote.info())
        except IOError, err:
            c.error = err
            return render('validation.error')
        except:
            return render('validation.error')
        return render('validation.result')
        
    def parseUploadedFile(self):
        #print request.POST['input_upload'].value
        #c.result = self.parser.parse(request.POST['input_upload'].value)
        try:
            c.result = self.parser.parse(request.POST['input_upload'].value)
        except:
            return render('validation.error')
        return render('validation.result')
