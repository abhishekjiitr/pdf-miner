import xml.etree.ElementTree as ET
import re
import nltk.corpus
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize,sent_tokenize
import enchant

# import EditDistance
# from NameExtractor import textToNames
# from EditDistance import nameemailpairtext
# from nltk import metrics,stem ,tokenize

Emails = []
Names = []
Text = []
SuperScripts = []

global AbsTop, AbsLeft
AbsTop=0
AbsLeft=0

'''
 Function: makeTree
 	creates an Element Tree from the content of .xml file

 Returns:
    None

 Parameters:
 	filename - the file which you want to create the Element Tree from.

'''
def makeTree(filename):
    #print "\ns>",filename
    global tree,root,lst,Emails,Names,Text,SuperScripts
    Emails = []
    Names = []
    Text = []
    SuperScripts = []
    try:
        tree = ET.parse(filename)
        root = tree.getroot()#ET.fromstring(input)
        lst = root[0].findall('text')
    except:
        print("Error Handled while making tree from xml.")
#print 'User count:', len(lst)
#print "--------------------------------------------------------"#root.tag

'''
 Function: isCandidate
 	utility function for isEmail

 Returns:
    True or False

'''
def isCandidate(string):
    if len(string)>6:
        return True
    return False

'''
 Function: isCandidate
 	utility function for isEmail

 Returns:
    True orFalse

'''
def valid(ch):
    return bool(re.search("[a-zA-Z0-9._%+-@]", ch))

'''
 Function: isEmail
 	returns True if input string is an email. Also append the string to Emails list.

 Returns:
    True - if input string is an email

 Parameters:
 	s - candidate email string

'''
def isEmail(s):
    try:
        global Emails
        s = s.replace("[at]", "@")
        if "@"  not in s:
            return False
        if "{" not in s and "}" not in s:
            s = s.split(" ")
            for chunk in s:
                if "@" in chunk:
                    s1 = chunk
                    break
            subway = ""
            for ch in s1:
                if valid(ch):
                    subway += ch
            Emails.append(subway.strip())
            return True
        i1 = s.index("{")
        i2 = s.index("}")
        names = s[i1+1:i2].split(",")
        names = [name.strip() for name in names]
        dom = s[i2+1:].split(" ")
        subdomain = ''
        for part in dom:
            if "@" in part:
                subdomain = part
        # print("$$"+str(dom)+"$$")
        # print(names)
        subd = ""
        if subdomain != '':
            for ch in subdomain:
                if valid(ch):
                    subd += ch
            names = [name.strip()+subd for name in names]
            Emails.extend(names)
            return True
        return False
    except:
        return False
    # x = list(string)
    # if '@' in x:
    #     Emails.append(re.findall('\S+@\S+',string))
    #     return True
    # return False

'''
 Function: isPaper
 	checks if the document is a research paper or not.

 Returns:
    True if document is a research paper.

 Parameters:
    no parameter

'''
def isPaper():
    global root
    x=0
    for child in root[0].findall('text'):
        #print  child.text
        global AbsTop
        string = child.text
        if not string == None:
            if 'BSTRACT' in (string).upper() :
                x+=1
            if 'NTRODUCTION' in (string).upper() :
                x+=1
            if 'EYWORDS' in (string).upper() :
                x+=1
            if 'SSN' in (string).upper() :
                x+=1
        else:
            for kid in child.iter():
                string = kid.text
                if not string == None:
                    if 'BSTRACT' in (string).upper() :
                        x+=1
                    if 'NTRODUCTION' in (string).upper() :
                        x+=1
                    if 'EYWORDS' in (string).upper() :
                        x+=1
                    if 'SSN' in (string).upper() :
                        x+=1
    if x>=2:
        return True
    else:
        return False

'''
 Function: getAbstop
 	set values of AbsTop and AbsLeft

 Returns:
    None

 Parameters:
 	No parameter

'''
def getAbstop():
    global root
    for child in root[0].findall('text'):
        #print  child.text
        global AbsTop
        string = child.text
        if not string == None:
            if 'BSTRACT' in (string).upper() :
                #print "xxxxx" , child.tag , child.attrib
                AbsTop = int(child.get('top'))
                AbsLeft = int(child.get('left'))
                #print AbsTop, AbsLeft
        else:
            for kid in child.iter():
                string = kid.text
                if not string == None:
                    if 'BSTRACT' in (string).upper() :
                        #print "xxxxx" , child.tag , child.attrib
                        AbsTop = int(child.get('top'))
                        AbsLeft = int(child.get('left'))
                        #print AbsTop, AbsLeft
                #print AbsTop,'\n  '
                #print child.get('top')#AbsHyt
#if type(string) == None:
#    return False
#el
'''
 Function: setPrimaryLists
    reads data and appends to respective lists.

 Returns:
    None

 Parameters:
 	No parameter

'''
def setPrimaryLists():
    #Text, SuperScripts
    for child in root[0].findall('text'):
        stri = child.text
        if stri == None:
            for kid in child.iter():
                stri = kid.text
                if not stri == None:
                    break
        if stri == None or stri == ' ':
            #print 'dadadad----------++++++++++'
            continue
        t = int(child.get('top'))
        l = int(child.get('left'))
        #print "#####"+AbsTop

        if isCandidate(stri) and t<AbsTop:
            #wordnet.synsets("word")
            #print t, AbsTop
            string = ''+stri.strip()
            string = string.lstrip(', ')
            if 'and ' in string[0:4].lower():
                #print "@@@@@@@@@@@@@@@@@@@@1" ,string,"||",
                string = string[4:]
                string = string.strip()
                #print string
            #     string[0:3].replace("AND ",'')
            #     string[0:3].replace("And ",'')
            # elif ' and ' in string.lower():
            w = string.split(' AND ')
            string = " , ".join(x.strip() for x in w if x.strip())
            w = string.split(' and ')
            string = " , ".join(x.strip() for x in w if x.strip())
            w = string.split(' And ')
            string = " , ".join(x.strip() for x in w if x.strip())

            if string:
                isEmail(string)
            # print  t,l,string
            tupl = (t,l,string,int(child.get('height')))#,child.attrib)
            Text.append(tupl)#str(t)+" "+str(l)+" "+string)
    #print '----------0000000000----------00000000000---'

    for child in root[0].findall('text'):
        string = child.text
        if string == None:
            for kid in child.iter():
                string = kid.text
                if not string == None:
                    break
        if string == None or string == ' ':
            #print 'dadadad----------++++++++++'
            continue
        t = int(child.get('top'))
        l = int(child.get('left'))
        #print "#####"+AbsTop
        if (not isCandidate(string)) and t<AbsTop:
            #print "***"+str(t < AbsTop),
            #print t, AbsTop
            #print  t,l,string
            string = string.strip()
            tupl = (t,l,string,int(child.get('height')))#,child.attrib)
            #tuplex = (t,l,string,int(child.get('font')))
            Text.append(tupl)#str(t)+" "+str(l)+" "+string)
            SuperScripts.append(tupl)
    # print '\n'
'''
 Function: SuperMatching
    sorts elements according to their position from top and left margin
    utility function to match information using SuperScripts - incomplete

 Returns:
    None

 Parameters:
 	No parameter

'''
def SuperMatching():
    global SuperScripts,Text
    for ex in SuperScripts:
        print(ex[0],ex[1],ex[2],ex[3])#Text
        searchClosest(ex[0],ex[1],Text,ex[3])
    Text.sort(key=lambda text: 100000*int(text[0])+int(text[1]))
    SuperScripts.sort(key=lambda text: 100000*int(text[0])+int(text[1]))
#Text.sort(key=lambda text: int(text[1]))

'''
 Function: searchClosest
    function to match superscripts with text elements - incomplete // not used yet 

 Returns:
    None

 Parameters:
 	top - position of a superscript
	left - position of a superscript
    Text - partially reduced text
    height - height of text element

'''

def searchClosest(top,left,Text,height):
    for item in Text:
        #val=(top+height-item[0]-item[3])
        val=(top-item[0])
        if val<5 and val>-20 and val!=0:
            print("$$$$$",item[0],item[1],item[2],item[3])
    #print '\n'


'''
 Function: reduceTextx
    removes the statements which do not contain required info

 Returns:
    string - containing statements probably having names or other details merged with ';'

 Parameters:
 	No parameter

'''
def reduceTextx():
    global Text
    tmp=''
    for item in Text:
        #line = item[2].split(' ')
        line = word_tokenize(item[2])
        n = 0
        nwords = 0
        previousChar = ''
        d = enchant.Dict("en_US")
        for word in line:
            if not bool(re.search(r'\d', word.lower())):
                #print word.lower(),
                if len(word)>1:
                    nwords += 1
                    if (not '.' in word) and d.check(word):#wordnet.synsets(word):
                        n+=1
                    # else:
                    #     print  "gj" ,   word
            else:
                nwords+=1
                n+=1
        if (not nwords == 0) and (n+0.0)/nwords < 0.6 and isCandidate(item[2]):
            # print 'xxxx', item[0],item[1],item[2],item[3]
            tmp+=item[2]+" ; "
    #print "ooooooooo\n",tmp
    return tmp

'''
 Function: callMe
    call only this function to get the required output
 	calls all the other required functions

 Returns:
    reduced text containing Names , list of Emails from the .xml file

 Parameters:
 	filename - name of file from which the text needs to be extracted.

'''
def callMe(filename):
    makeTree(filename)
    if isPaper():
        getAbstop()
        setPrimaryLists()
        texting = reduceTextx()
        #if len(Emails)!=0:
        # tx = word_tokenize(texting)
        # print tx
        if len(Emails)!=0:
            # print "\n>>>",filename
            # print "$$$$$$",Emails
            #print "\n",texting
            return texting,Emails
    # w = textToNames(texting)
    # print w
    #print nameemailpairtext(texting)
    # print '\n------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--------\n'
    return None,[]
    #print "?????" ,texting
if __name__ == "__main__":
    print('\n------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--------\n')

    callMe("/media/rishabh/2F1D-83B3/pdf/1916737645Chapter_15.pdf.xml")
    # callMe("/media/ambar/2F1D-83B3/xml/0203csit9.pdf.xml")
    # callMe("/media/ambar/2F1D-83B3/xml/3313ijdkp01.pdf.xml")
    # callMe("/media/ambar/2F1D-83B3/xml/3313ijdkp02.pdf.xml")
    # callMe("/media/ambar/2F1D-83B3/xml/3313ijdkp04.pdf.xml")
    # callMe("/media/ambar/2F1D-83B3/xml/6613884t.pdf.xml")
    # callMe("out1.xml")
    # callMe("out2.xml")
    # callMe("jensen-neville-nas2002.pdf.xml")
    # callMe("V4_I1_2015_paper4.pdf.xml")



    #makeTree("out3")
    #getAbstop()
    #setPrimaryLists()
    #for item in Text:
    #    print item[0],item[1],item[2]
    #print '\n'
    #reduceTextx()
    #searchClosest(173,377,Text)
    #searchClosest(225,368,Text)
    #searchClosest(240,358,Text)
    #searchClosest(256,377,Text)
    #searchClosest(271,346,Text)
    #searchClosest(286,248,Text)
    #print '\n'
