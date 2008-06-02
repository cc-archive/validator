import httplib
from StringIO import StringIO
import HTMLParser
import encutils, chardet
import BeautifulSoup, tidy

# detect encoding (headers, declaration, meta) or force chosen
# clean the code (Beautiful Soup, Tidy)
# parse license information

class Parser:

    def _fakeRes(self, content):
        "build a fake HTTP response"
        class FakeRes:
            def __init__(self, content):
                fp = StringIO(content)
                self._info = httplib.HTTPMessage(fp)
                
            def info(self):
                return self._info
        return FakeRes(content)    
    
    def parse(self, text, header=None):
        """ Detect character encoding """
        if header:
            res = encutils.getEncodingInfo(self._fakeRes(header), text)
        else:
            res = encutils.getEncodingInfo(text=text)
        meta_mimetype, meta_encoding = encutils.getMetaInfo(text=text)
        if res.encoding:
            encoding = res.encoding
        elif meta_encoding:
            encoding = meta_encoding
        else:
            encoding = chardet.detect(text)['encoding']
        if encoding:
            try:
                text.encode(encoding)
            except (UnicodeEncodeError, UnicodeDecodeError):
                """ The declared encoding does not match the actual one """
                encoding = None
        else:
            """ No encoding found """
            pass
        """ Clean the code """
        
        exit((str(header), error, text, encoding, encutils.getMetaInfo(text=text), res.encoding, res))

