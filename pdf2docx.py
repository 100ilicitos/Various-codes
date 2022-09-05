# Pdf transform to docx
# by Busyman.Inc

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pdf2docx import Converter
pdf = 'cv_PT.pdf'
docx = 'PT.docx'
cv = Converter(pdf)
cv.convert(docx)
cv.close()
