import os
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
#read files

corpusroot = "./presidential_debates"
alldebates=""

for filename in os.listdir(corpusroot):
    file = open(os.path.join(corpusroot, filename), "r", encoding='UTF-8')
    doc = file.read()
    file.close() 
    doc = doc.lower()
    alldebates+=doc
    

stemmer=PorterStemmer()       
tokenizer=RegexpTokenizer(r'[a-zA-Z]+')
tokens=tokenizer.tokenize(alldebates)
#store stemmed words in list_Stem
list_stem =[stemmer.stem(word) for word in tokens]
tfidfweights=[0] * len(list_stem)
words = dict(zip(list_stem,tfidfweights))

print()

