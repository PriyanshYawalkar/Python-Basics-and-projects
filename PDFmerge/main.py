import PyPDF2

pdfiles = ["leave.pdf", "bpl.pdf"] # you can type multiple name of pdf inside square brackets
merger = PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write('merger.pdf')