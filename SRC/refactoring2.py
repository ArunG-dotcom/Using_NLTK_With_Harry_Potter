# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 19:12:43 2021

@author: reach
"""
#------------------------------------------------------------------------------
# Nan - not a number
#importing packages
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk import everygrams
from collections import defaultdict
import pandas as pd
import numpy as np
import re

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('average_perceptron_tagger')
nltk.download('maxent_treebank_pos_tagger')
#------------------------------------------------------------------------------
def get(filename, bookname):

#opening,reading,translating(replacing),and spliting the sorcerors stone file
    with open(filename,"r",encoding='utf8',errors="ignore") as f:
        text_list = f.read().lower().split()
        
    #--------------------------------------------------------------------------  
    #takes out punctuation lines 32 - 45 
    #stopwords is a list of common words that can be removed
    stop_list = []
    stop_words = list(stopwords.words("english"))
    for word in text_list:
        if word in stop_words:
            pass
        else:
            stop_list.append(word) 
    #--------------------------------------------------------------------------       
    #translation is a built in function which helps with changing
    #the characters which I am using to remove punctuation.   
    trans = str.maketrans("","",'~!@#$%^&*()`,.<>/?\\|[]{};-\n\':"') 
    strip_list = []
    for word in stop_list:
        word = word.translate(trans)
        strip_list.append(word) # adding the single item to a existing list
    #--------------------------------------------------------------------------
    #stem helps with breaking the word down to its base/root
    stem_list = []
    ss = SnowballStemmer("english")
    for word in strip_list:
        word = ss.stem(word)
        stem_list.append(word)
    #--------------------------------------------------------------------------
    #Returns all possible ngrams generated from the text.
    ngram = list(everygrams(stem_list, min_len = 3, max_len = 5))  
    # adds any item to the exisisting list/dictionary
    count_dict = defaultdict(lambda: 0)
    # counting the number of ngrams.
    for tuples in ngram:
        count_dict[tuples] += 1
    
    df = pd.DataFrame(count_dict, index = [bookname])
            
    return df
#------------------------------------------------------------------------------
if __name__=="__main__":
    # getting the sorcerors stone file
    df1 = get('../Data/sorcerors_stone.txt', 'sorcerors_stone') 
    # getting the fellowship_of_ring
    df2 = get('../Data/fellowship_of_ring.txt', 'fellowship_ring')
    ## getting the unkown file
    df3 = get('../Data/unknown.txt','unknown')
    #--------------------------------------------------------------------------
    # concat combines the text from Df1,Df2,Df3
    df = pd.concat([df1,df2,df3]).fillna(0)
    #--------------------------------------------------------------------------
    # distance from orgin - linealg function
    # this line helps calculate the distance between the unkown and the
    #sorcerors stone
    d = np.linalg.norm(df.loc['sorcerors_stone'] - df.loc['unknown']) 
    print("The distance between the sorcerors stone and the unknown", int(d))

    # distance from orgin - linealg function
    #The loc property is used to access a group of rows and columns by label(s)
    #or a boolean array. . loc[] is primarily label based, but may also be used
    #with a boolean array.
    #This line helps calculate the distance between the unkown and the
    #fellowship_of_ring
    c = np.linalg.norm(df.loc['fellowship_ring'] - df.loc['unknown']) 
    print("The distance between the fellowship ring and the unknown", int(c))

    print("The unknown book is more similar to the sorcerors stone book.")
    #--------------------------------------------------------------------------
    
                      


  

   
              

    
                      


  

   





                    
                  


  

   
