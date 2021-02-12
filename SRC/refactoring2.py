# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 19:12:43 2021

@author: reach
"""
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk import everygrams
from collections import defaultdict
import pandas as pd
import numpy as np
import re

def get(filename):
    #Setting the path to the first book in the harry potter series.

    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('average_perceptron_tagger')
    nltk.download('maxent_treebank_pos_tagger')

    
    

#   opening,reading,translating(replacing),and spliting the sorcerors stone file
    with open(filename,"r",encoding='utf8',errors="ignore") as f:
        text_list = f.read().lower().split()
           
    stop_list = []
    stop_words = list(stopwords.words("english"))
    for word in text_list:
        if word in stop_words:
            pass
        else:
            stop_list.append(word)
        
    trans = str.maketrans("","",'~!@#$%^&*()`,.<>/?\\|[]{};-\n\':"') 
    strip_list = []
    for word in stop_list:
        word = word.translate(trans)
        strip_list.append(word)
            
    stem_list = []
    ss = SnowballStemmer("english")
    for word in strip_list:
        word = ss.stem(word)
        stem_list.append(word)
    
    ngram = list(everygrams(stem_list, min_len = 3, max_len = 5))
    
    count_dict = defaultdict(lambda: 0)
    for tuples in ngram:
        count_dict[tuples] += 1
    
    df = pd.DataFrame(count_dict, index = ["sorcerors_stone"])
            
            
            
            
            
            
            
            
            
            
            
            
    print(df)

if __name__=="__main__":
    print(get('../Data/sorcerors_stone.txt'))





                    
                  


  

   