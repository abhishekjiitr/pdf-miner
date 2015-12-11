import os,downloadpdf
f=open('pdf2.txt','r')

for line in f.readlines():
    try:
        downloadpdf.download_pdfs([line.rstrip()],0)
    except:
        pass
