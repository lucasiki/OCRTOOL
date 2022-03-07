import re
from datetime import date, datetime
import datetime
from pytesseract import image_to_string
import PIL
from PIL import Image
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from io import StringIO
from pdfminer.pdfpage import PDFPage
from pdf2image import convert_from_path
import pytesseract as pt  
import PyPDF2
import textract


def ler_textract(arquivo):
    text = textract.process(arquivo, method='tesseract', language='por')

    return text.lower()

def ler_py2pdf(arquivo):

    pdfFileObj = open(arquivo,'rb')

    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    num_pages = pdfReader.numPages

    count = 0
    text = ""

    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count +=1
        text += pageObj.extractText()

    return text.lower()

def ler_miner(arquivo):
    #CAMINHO PDF
    caminho_PDF = arquivo
    resource_manager = PDFResourceManager(caching=True)
    out_text = StringIO()
    codec = 'utf-8'
    laParams = LAParams()
    text_converter = TextConverter(
        resource_manager, out_text, laparams=laParams)
    fp = open(caminho_PDF, 'rb')
    interpreter = PDFPageInterpreter(resource_manager, text_converter)
    for page in PDFPage.get_pages(fp, pagenos=set(), maxpages=0, password="", caching=True, check_extractable=True):
        interpreter.process_page(page)
    text = out_text.getvalue()
    fp.close()
    text_converter.close()
    out_text.close() 


    return text.lower() 

def ler_tesseract(arquivo):
    #CAMINHO PDF
    pdf_name = arquivo
    doc = convert_from_path(pdf_name)
    text = ''
    for page_number, page_data in enumerate(doc):
        txt = pt.image_to_string(page_data, lang='por')
        print(page_number)
        
        text = ''.join((text, txt)) 

    return text.lower()        
        

