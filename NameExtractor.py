
import nltk
from nltk import pos_tag
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize,sent_tokenize
from PyPDF2 import PdfFileWriter,PdfFileReader
import pyPdf
import re

regex = re.compile("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                    "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                    "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)")

def get_emails(s):
	a=re.findall(regex,s)
	b=list()
	for a1 in a:
		b.append(a1[0])
	return b

def listofnames(filename):
    text = " "
    # pdf = PdfFileReader(open(filename,'rb'))
    # p = pdf.getPage(0)
    # try:
    #     p2 = pdf.getPage(1)
    # except:
    #     pass
    #
    # outfile = PdfFileWriter()
    # outfile.addPage(p)
    #
    # # If the first two pages should be considered then uncomment the following
    #
    # # if not p2:
    # #     pass
    # # else:
    # #     outfile.addPage(p2)
    #
    # index = 0
    #
    # with open('/Users/SHARAN/Downloads/test'+str(index)+'.pdf','wb+') as f2:
    #     outfile.write(f2)
    f3 = pyPdf.PdfFileReader(open(filename,'rb'))
    # index += 1
    for i in range(2):
        try:
            text+= f3.getPage(i).extractText()
        except:
            continue
    text_to_lower = text.lower()
    text_to_lower = text_to_lower.replace('\n',' ')
    num = 0
    listofemails = get_emails(text)
    list_of_proper_nouns = [' ']

    list_of_keywords = word_tokenize(text_to_lower)
    if 'issn' in list_of_keywords:
        num += 2
    if 'keywords' in list_of_keywords:
        num += 1
    if 'abstract' in list_of_keywords:
        num += 1
    if 'introduction' in list_of_keywords:
        num += 1
    if 'keyword' in list_of_keywords:
        num+= 1

    if num < 2:
        print("not a journal")
        return (['stderror@iitr.com '],['James Thomason'])
    list_of_tokens = word_tokenize(text.replace('\n',' '))
    list_of_tokens_lower = word_tokenize(text_to_lower)
    tagged_lower = nltk.pos_tag(list_of_tokens_lower)
    tagged = nltk.pos_tag(list_of_tokens)
    if len(tagged) != len(tagged_lower):
        print "Length is unequal"
    global sometext
    sometext = str()
    for i in range(len(tagged)):
        try:
            if tagged[i][0] == '(' or tagged[i][0] == ')':
                continue
            if '@' in tagged[i][0]:
                    continue
            if tagged[i][1] == "NNP" and (tagged_lower[i][1] == "NNP" or tagged_lower[i][1] == 'NN'):
                if not wordnet.synsets(tagged_lower[i][0]):
                    sometext = sometext +' '+ str(tagged[i][0])
            else:
                if sometext != '':
                    list_of_proper_nouns.append(sometext)
                sometext = ''
        except:
            print "Some error "
            continue
    return (listofemails,list_of_proper_nouns)
