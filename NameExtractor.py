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
        #text_to_lower = text_to_lower.replace('\n',' ')

        #print '>',text
        nameListAmbar.append(text)
        # n = 0
        # nwords = 0
        # word=text.split()
        # print word
        # for word in text:
        #
                            # list_of_tokens = word_tokenize(modifiedText)
                            #
                            # list_of_tokens_lower = word_tokenize(modifiedText.lower())
                            # list_of_tokens = text.split()
                            # list_of_tokens_lower = text_to_lower.split()
                            #
                            # for token in list_of_tokens:
                            #     #print "----",token
                            #
                            #     if d.check(token.lower()):
                            #         list_of_tokens_lower.remove(token.lower())
                            #         list_of_tokens.remove(token)
                            #
                            # # for token in list_of_tokens_lower:
                            # #     print '>>>', token
                            # try:
                            #     list_of_tokens.remove("(")
                            #     list_of_tokens.remove(")")
                            #     list_of_tokens_lower.remove("(")
                            #     list_of_tokens_lower.remove(")")
                            # except:
                            #     pass
                            #
                            # tagged_lower = nltk.pos_tag([w.replace('.','') for w in list_of_tokens_lower])
                            # tagged = nltk.pos_tag(list_of_tokens)
                            #
                            # if len(tagged) != len(tagged_lower):
                            #     print "Length is unequal"
                            # global sometext
                            # sometext = ''
                            # for i in range(len(tagged)):
                            #     try:
                            #         if tagged[i][0] == '(' or tagged[i][0] == ')':
                            #             continue
                            #         if '@' in tagged[i][0]:
                            #                 continue
                            #         if tagged[i][1] == "NNP" and (tagged_lower[i][1] == "NNP" or tagged_lower[i][1] == 'NN'\
                            #         or tagged_lower[i][1] == 'NNS' or tagged_lower[i][1] == "NNPS"):
                            #             if not d.check(tagged_lower[i][0]):
                            #                 sometext = sometext +' '+ str(tagged[i][0])
                            #         else:
                            #             if sometext != '':
                            #                 list_of_proper_nouns.append(sometext)
                            #             sometext = ''
                            #     except:
                            #         print "Some error "
                            #         continue
                            #
                            # for noun in list_of_proper_nouns:
                            #     if len(noun.strip().split()) == 1 and len(noun.strip()) < 4:
                            #         list_of_proper_nouns.remove(noun)
    #print '...',list_of_proper_nouns
    #print nameListAmbar#listText
    #print "@@@@@@",list(set(nameListAmbar))
    #return (listofemails,list_of_proper_nouns)
    return list(set(nameListAmbar))#list_of_proper_nouns)
