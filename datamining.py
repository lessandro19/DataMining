# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 21:21:00 2020

@author: Less
"""

import os
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from collections import Counter
import time
import math
start = time.time()
#import pdb; pdb.set_trace()
#create an array that will hold our stems
#This List holds all of our document names
DocumentNames=[]
#This List holds a list of lists where each element of the list corresponds to the list of words for that specific document
AllDocuments=[]
N=0
#This function adds all the words of the current doc, to our list of documents and their words
def AppendTerms(tokens):
    AllDocuments.append(tokens)

corpusroot = "./presidential_debates"
#read all files
for filename in os.listdir(corpusroot):
    file = open(os.path.join(corpusroot, filename), "r", encoding='UTF-8')
    doc = file.read()
    file.close() 
    #Make the document to lowercase and tokenize it
    doc = doc.lower()
    tokenizer=RegexpTokenizer(r'[a-zA-Z]+')
    tokens=tokenizer.tokenize(doc)
    #Add our tokens to our existing list of all words, also save the names of all the documents
    DocumentNames.append(filename)
    #Append the tokens to our list 
    #Perform stemming on the tokens and store it in the list_stem, then add it to our stemmed tokens
    stemmer=PorterStemmer()
    AppendTerms([stemmer.stem(word) for word in tokens])
    
#This will hold our unique words that will be our keys for our TF-IDF vector

N=len(DocumentNames)
#Convert to weighted frequency  


UniqueTerms=[]    

for document in AllDocuments:
    uniquedoc=Counter(document)
    UniqueTerms.append(uniquedoc)  
for document in UniqueTerms:
    for word in document:
        document[word]=1+(math.log10(document[word]))
        
def getidf(token):
    Occurrences=[0]*N
    iterator=0
    idf=-1
    for DocumentDictionary in UniqueTerms:
        if token in DocumentDictionary:
            Occurrences[iterator]=1
        iterator=iterator+1
        
    docsoccurredin=sum(Occurrences)
    if docsoccurredin!=0:
        idf=math.log10(N/docsoccurredin)
    return idf

#calculate the TF-IDF weight and store it in a dictionary called TF
length=0
for document in UniqueTerms:
    
    for word in document:
        idf=getidf(word)
        document[word]=document[word]*idf
        length=length+(document[word]*document[word])
 
magnitude=math.sqrt(length)

for document in UniqueTerms:
    for word in document:
        document[word]=document[word]/magnitude
        
       

        
        
        
         
    
def getweight(document,term):
    x=DocumentNames.index(document)
    indexeddocument=UniqueTerms[x]
    if term in indexeddocument:
        return indexeddocument[term]
    else:
        return 0
    
print("%.12f" % getweight("2012-10-03.txt","health"))