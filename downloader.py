import pickle
from os import listdir, sep
from os.path import isfile, join
import downloadpdf.download_pdf

onlyfiles =[f2 for f2 in listdir("pickled_links") if isfile(join("pickled_links", f2))]

def call():
    f1 = open("mine"+os.sep+"archive"+os.sep+"pdf.txt")
    for line in f1.readlines():
        some_list = list(line)
        try:
            download_pdf(some_list,0)
        except:
            print("Some error occured")
            continue

call()
