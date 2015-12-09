# -*- coding: utf-8 -*-
import pyPdf
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

pdf = pyPdf.PdfFileReader(open("test.pdf", "rb"))
text = ""
for page in pdf.pages:
    text += (page.extractText())

st = StanfordNERTagger('/home/jaisingh/stanford-ner-2014-06-16/classifiers/english.all.3class.distsim.crf.ser.gz',
					   '/home/jaisingh/stanford-ner-2014-06-16/stanford-ner.jar')

# text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'

tokenized_text = word_tokenize(text)
classified_text = st.tag(tokenized_text)

# print(classified_text)
persons = []
for entity in classified_text:
    if entity[1] == "PERSON":
        print(entity)
        persons.append(entity[0])
