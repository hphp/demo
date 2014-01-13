################################################################
### Text I/O
################################################################
import unicodedata
import re
import codecs
from numpy import *
import chars
replacements = chars.replacements

def read_text(fname,nonl=False,normalize=True):
    """Read text. This assumes files are in unicode.
    By default, it removes newlines and normalizes the
    text for OCR processing with `normalize_text`"""
    with codecs.open(fname,"r","utf-8") as stream:
        result = stream.read()
    if nonl and len(result)>0 and result[-1]=='\n':
        result = result[:-1]
    if normalize:
        result = normalize_text(result)
    return result

def write_text(fname,text,nonl=0,normalize=1):
    """Write text. This assumes files are in unicode.
    By default, it removes newlines and normalizes the
    text for OCR processing with `normalize_text`"""
    if normalize:
        text = normalize_text(text)
    with codecs.open(fname,"w","utf-8") as stream:
        stream.write(text)
        if not nonl and text[-1]!='\n':
            stream.write('\n')

def normalize_text(s):
    """Apply standard Unicode normalizations for OCR.
    This eliminates common ambiguities and weird unicode
    characters."""
    s = unicode(s)
    s = unicodedata.normalize('NFC',s)
    s = re.sub(ur'\s+(?u)',' ',s)
    s = re.sub(ur'\n(?u)','',s)
    s = re.sub(ur'^\s+(?u)','',s)
    s = re.sub(ur'\s+$(?u)','',s)
    for m,r in replacements:
        s = re.sub(unicode(m),unicode(r),s)
    return s

