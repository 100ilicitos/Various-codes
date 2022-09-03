# Pdf transform to docx
# by Busyman.Inc

import os
from pdf2docx import Converter
pdf = 'PT.pdf'
if os.path.exists(pdf):
        docx = 'PT.docx'
        cv = Converter(pdf)
        cv.convert(docx)
        cv.close()
else:
        print("exit")
