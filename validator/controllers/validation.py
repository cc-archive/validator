import logging
import urllib
import encutils

from validator.lib.base import *
from validator.lib.parser import *

log = logging.getLogger(__name__)

class ValidationController(BaseController):

    def __init__(self):
        self.parser = Parser()

    def index(self):
        return render('validation.index')
    
    def parseDirectInput(self):
        self.parser.parse(request.POST['input'])
        
    def parseOnlineDocument(self):
        try:
            remote = urllib.urlopen(request.POST['input'])
            self.parser.parse(remote.read(), header=remote.info())
        except IOError:
            pass
    
    def parseUploadedFile(self):
        self.parser.parse(request.POST['input'].value)
    
        """
        c.encoding = None
        if 'input' in request.POST and request.POST['input'].strip() != '':
            c.code = request.POST['input']
            try:
                c.encoding = encutils.getEncodingInfo(text=c.code)
            except HTMLParseError:
                c.error = "Error parsing the directly input code."
        elif 'link' in request.POST and request.POST['link'].strip() != '':
            try:
                c.code = urllib.urlopen(request.POST['link']).read()
                c.encoding = encutils.getEncodingInfo(url=request.POST['link'])
            except IOError, e:
                c.error = e[1]
            except HTMLParseError:
                c.error = "Error parsing the remote document."
        elif 'file' in request.POST:
            c.code = request.POST['file'].value
            try:
                c.encoding = encutils.getEncodingInfo(text=c.code)
            except HTMLParseError:
                c.error = "Error parsing the upload file."
        
        if str(c.encoding) != '':
            try:
                c.code = unicode(c.code, str(c.encoding), errors='strict')
            except TypeError:
                c.code
        else:
            c.encoding = repr(c.encoding) #'Unicode'
        
        return render('dummy.index')
        """
        
