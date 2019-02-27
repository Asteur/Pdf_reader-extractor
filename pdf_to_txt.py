from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    fstr = ''
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,    password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

        str = retstr.getvalue()
        fstr += str

    fp.close()
    device.close()
    retstr.close()
    return fstr
