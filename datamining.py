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
import math
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


#Create a list/dictionary that will hold all of our unique terms. This will be a list of dictionaries
UniqueTerms=[]    

#this for-loop creates a dictionary from each document. The counter function gets the unique words which are the "keys" and the number
#of times they occured as "values". UniqueTerms is now a list of term-frequency dictionaries for each document
for document in AllDocuments:
    uniquedoc=Counter(document)
    UniqueTerms.append(uniquedoc)  
    


#This function gets the inverse document frequency of a term and returns it         
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

#For each word in our term-frequency dictionary, we need to calculate the TF-IDF values for each word

#Create a magnitude list to keep track of the magnitude of each document    
magnitude=[]
#iterate through each dictionary in our list of term-frequency dictionaries
for document in UniqueTerms:
    #length will keep track of the current document's TF-IDF vector magnitude
    length=0
    for word in document:
        #for each word in our document term-frequency dictionary, find the idf
        idf=getidf(word)
        document[word]=1+(math.log10(document[word]))
        document[word]=document[word]*idf
        length=length+(math.pow(document[word],2))
 
    magnitude.append(math.sqrt(length))
    

iterator=0
for document in UniqueTerms:
    for word in document:
        document[word]=document[word]/magnitude[iterator]
    iterator=iterator+1
       

        
        
        
         
    
def getweight(document,term):
    x=DocumentNames.index(document)
    indexeddocument=UniqueTerms[x]
    if term in indexeddocument:
        return indexeddocument[term]
    else:
        return 0
    
def query(qstring):
    #create a list based on the words in our query
    qstring=qstring.lower()
    stringvector=qstring.split()
    #use the counter dictionary method to get the term frequency for each term in the query
    WordCountsInQString=Counter(stringvector)
    #create a variable that tracks the magnitude
    length=0
    
    #for each term(key) in our string, we need to do weight frequency for each term
    
    for key in WordCountsInQString:
        WordCountsInQString[key]=1+math.log10(WordCountsInQString[key])
        #Square the frequency and add it to the magnitude
        length=length+(math.pow(WordCountsInQString[key],2))
    
    #take the square root of our length vector
    
    
    
    
    
    magnitude=math.sqrt(length)
    #divide each weighted termfrequency by the magnitude to normalize our tfidf vector     
    for key in WordCountsInQString:
        WordCountsInQString[key]=WordCountsInQString[key]/magnitude
        
        
    #postings list is a a list of tf-idf lists for each word
    postingslist=[]
   
    #iterate through each word in the list
    for Word in WordCountsInQString:
        #create a WordList list that will keep track of the current term's TF-IDF weights across all documents
        TFIDFValuesforSpecificTerm=[]
        #clear it just incase it has any previous data
        TFIDFValuesforSpecificTerm.clear()
        
        #iterate through all of our TF-IDF vectors
        
        for document in UniqueTerms:
            #set our value to negative 1 as default
            value=0
            #check if the word is in that documents TF-IDF vector, if so get the weight
            if Word in document:
                value=document[Word]
            #append the TF-IDF weight to our vector of tf-idf weights
            TFIDFValuesforSpecificTerm.append(value)
            
        #once we have all the TF-IDF vectors for a word, we add it to our QueryList so we can iterate through it later
               
        postingslist.append(TFIDFValuesforSpecificTerm)
    
    #iterate through each term's tf-idf vector
    
    TopTenIDFpostinglist=[]
    documentnames=[]
    #this loop gets the top 10 tf-idf vectors for tf-idf vector in our postings list
    for tfidfvector in postingslist:
        #create a list of the top 10 tfidfvectors
        TopTenVal=sorted(tfidfvector, reverse=True)[:10]
        index=[]
        #iterate through each tfidf vector in our toptenvalues vector and get it's index (the document it belongs to)
        for val in TopTenVal:
            
            index.append(DocumentNames[tfidfvector.index(val)])
            
        TopTenIDFpostinglist.append(TopTenVal)
        documentnames.append(index)
    
    #now that we have our list of each term's top 10 tf-idf list(TopTenIDFpostinglist) and their corresponding documents(documetnames)
    #we need to find which documents d appear in the top-10 elements of each token in our query
    
    #case 1:check whether a document appears in all 
    
    
    
    return 'none', 0
        

print("(%s, %.12f)" % query("terror attack"))
        
        
    
            
            