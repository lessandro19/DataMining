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
    DocumentNames+=filename
    #Append the tokens to our list 
    #Perform stemming on the tokens and store it in the list_stem, then add it to our stemmed tokens
    stemmer=PorterStemmer()
    AppendTerms([stemmer.stem(word) for word in tokens])
    
#This will hold our unique words that will be our keys for our TF-IDF vector
TermFrequencies=[]
for document in AllDocuments:
    #create 
    TermFrequencies.append(Counter(document))

N=len(DocumentNames)
#Convert to weighted frequency  

#Go through each list of term frequencies
for DocumentDictionary in TermFrequencies:
    #go through each specific term
    for key in DocumentDictionary:
        #perform the weighted tf transformation
        if DocumentDictionary[key]!=0:
            DocumentDictionary[key]=1+math.log10(DocumentDictionary[key])
#Go through each list of term frequencies            
for DocumentDictionary in TermFrequencies:
    #Go through each specific term
    length=len(DocumentDictionary)
    for key in DocumentDictionary:
        #dft will keep track of the document frequency for our term
        dft=0
        #Create another loop that iterates through our Documents
        for x in TermFrequencies:
            #if the term exists in a Document(ie the key is valid)increment our document frequency
            if key in x:
                dft=dft+1
        #Calculate the TF-IDF , then divide it by the magnitude of the vector        
        DocumentDictionary[key]=(DocumentDictionary[key]*math.log10(N/dft))/length



        
    
 
       
  
    
end=time.time()
print(end-start)
