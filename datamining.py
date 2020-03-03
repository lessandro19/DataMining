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
start = time.time()
#create an array that will hold our stems
list_stem=[]
#This List holds all of our document names
DocumentNames=[]
#This List holds a list of lists where each element of the list corresponds to the list of words for that specific document
ListOfAllTerms=[]

#This function adds all the words of the current doc, to our list of documents and their words
def AppendTerms(tokens):
    ListOfAllTerms.append(tokens)


    
    
    




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
    list_stem+=[stemmer.stem(word) for word in tokens]
    AppendTerms(list_stem)
    
    
#this function calculates the document frequency
def documentsTermOccuredIn(term,vectorofdocuments):
    #create our vector of booleans representing whether a term occurred in aspecifc doc or not
    incidencevector=[0]*len(vectorofdocuments)
    x=0
    #iterate through each documen
    for document in vectorofdocuments:
        #iterate through each word that is in each document
        for word in document:
            #check if the word is the same as the term, if so add 1 to the incidence vector
            if term==word:
                incidencevector=incidencevector+1       
         x=x+1
    
var=0 
#iterate through our documents
for x in ListOfAllTerms:
    currentdoc=ListOfAllTerms[var]
    #create a dictionary of the terms for a specific document
    uniqueterms=Counter(currentdoc)
    #N represents the number of documents, which is found by getting the size of our Documents vector
    N=len(DocumentNames)
    #iterate through each word in our specific document
    for y in currentdoc:
        currentterm=currentdoc[y]
        #pass the currentterm and check how many documents the currentterm occurent in
        incidencevector=documentsTermOccurredIn(currentterm,ListOfAllTerms)
    var=var+1
    
    


end=time.time()
print(end-start)
