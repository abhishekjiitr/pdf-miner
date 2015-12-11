from nltk import metrics,stem ,tokenize
from NameExtractor import listofnames,get_emails
# stemmer = stem.PorterStemmer()
#
# def normalize(s):
#     words = tokenize.wordpunct_tokenize(s.lower().strip())
#     return ' '.join([stemmer.stem(w) for w in words])

#No use of normalization currently
def match(email,list_of_names):
    editdistance = 1000
    name = ' '
    for i in range(len(list_of_names)):
        if len(list_of_names[i].split()) > 1:
            subnames = list_of_names[i].split()
            subnames = [w.replace('.','') for w in subnames]
            mindistance = 1000
            for j in range(len(subnames)):
                distance = metrics.edit_distance(email,subnames[j])
                if distance < mindistance:
                    mindistance = distance
            if mindistance < editdistance:
                editdistance = mindistance
                name = list_of_names[i]
        else:
            distance = metrics.edit_distance(email,list_of_names[i])
            if distance < editdistance:
                editdistance = distance
                name = list_of_names[i]
    return name

def nameemailpair(filename):
    thedict = dict()
    emailList,properNouns = listofnames(filename)
    for email in emailList:
        firstemail = email.split('@')[0]
        thedict[email] = match(firstemail,properNouns)
    return thedict


# print match('ambar.ucs2014',['sharanpreetsingh','sharan preet singh','tarun kumar','sharn','abhishek jaisingh','ambar zaidi','zaidi'])
