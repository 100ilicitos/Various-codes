# Extract text from pdf
# By Busyman.InC

import PyPDF2

pdf = open("cv_PT.pdf", "rb")
reader = PyPDF2.PdfFileReader(pdf)
page = reader.getPage(0)
print(page.extractText())
