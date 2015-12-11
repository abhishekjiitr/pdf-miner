import os,downloadpdf
f=open('pdf3.txt','r')

for line in f.readlines():
    try:
        downloadpdf.download_pdfs([line.rstrip()],0)
    except:
        pass
