import pickle
import os
from os import listdir, sep
from os.path import isfile, join
import downloadpdf

f=open('pdf1.txt','r')

for line in f.readlines():
    #try:
    downloadpdf.download_pdfs([line.rstrip()],0)
    # except:
    #     print("Some error occured")
    #     continue
# onlyfiles =[f2 for f2 in listdir("pickled_links") if isfile(join("pickled_links", f2))]
# # print (onlyfiles)
# list_of_list_of_pdfs = list([' '])
#
# def call():
#     for i in range(4000):
#         for j in range(len(onlyfiles)):
#             try:
#                 downloadpdf.download_pdfs( pickle.load(open(os.path.join(os.getcwd()+os.sep+'pickled_links',onlyfiles[j]),'rb')),i)
#             except:
#
#                 continue
# call()
