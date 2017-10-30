import nltk
from nltk import pos_tag
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize,sent_tokenize
from PyPDF2 import PdfFileWriter,PdfFileReader
import re
import enchant

'''
 Function: get_emails
 	removes emails from input text

 Returns:
    b - list of emails
    modified_s - text without emails

 Parameters:
 	s - string : reduced text with statements merged with ';'

'''

# regex is the regular expression for finding out emails 
# out of streams of characters separated by whitespaces
regex = re.compile("([a-zA-Z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+\/=?^_`"
                    "{|}~-]+)*(@|\sat\s)(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?(\.|"
                    "\sdot\s))+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)")
def get_emails(s):
	a=re.findall(regex,s)
	b=list()
	for a1 in a:
		b.append(a1[0])
	modified_s = re.sub("[^;]*?([a-zA-Z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+\/=?^_`""{|}~-]+)*(@|\sat\s)(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?(\.|""\sdot\s))+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?).*?;",' ',s)
	return b,modified_s;

'''
 Function: textToNames
    extracts possible names from processed input text

 Returns:
    list - list of possible names

 Parameters:
    textIn - string : reduced text with statements merged with ';'

'''

def textToNames(textIn):

    listofemails,modifiedText = get_emails(textIn)
    list_of_proper_nouns = []
    modifiedText = modifiedText.replace(',',';')
    listText = modifiedText.split(';')
    # for ee in Emails:
    #     print ee
    # print "pp", modifiedText
    # textIn = textIn.replace(',',';')
    # listText = textIn.split(';')
    d = enchant.Dict("en_US")

    nameListAmbar =[]

    for text in listText:
        # text = text.strip()
        # if len(text)==0:
        #     continue
        if len(text.strip())==0:
            listText.remove(text)
            continue
        text = text.replace('\n',' ')
        text = text.strip()
        text_to_lower = text.lower()

        nameListAmbar.append(text)
  
    return list(set(nameListAmbar))#list_of_proper_nouns)
