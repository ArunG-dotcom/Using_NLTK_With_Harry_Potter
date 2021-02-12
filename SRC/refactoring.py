# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 16:06:46 2020

@author: reach
"""


import codecs
from operator import itemgetter

filename = input("What file would you like to open? (please type the exact name)")
#used to open and format the file ------------------

opened_file = codecs.open(filename, "r", encodings = 'utf8', errors="ignore")
txtfile = opened_file.read()
opened_file.close()

#gets rid of filler words ---------------------
filler_words = ['the','a','to','and','i','it','that','is','you','i','of','your']
def filler_removal(txt):
    for filler in filler_words:
        txt = txt.replace(filler,"")
    return txt

txtfile = filler_removal(txtfile)

#makes everything lowercase and puts the words in a list-------------
def punctuation_removal(txt):
    for punctuation in '~!@#$%^&*()`,.<>/?\\|[]{};\':"':
        txt = txt.replace(punctuation,'')
    return txt.lower().split()

txtfile = punctuation_removal(txtfile)


def count_ngrams(ngrams):
    for word_num in range(len(txtfile)):
        for gram_length in range(4):
            if word_num . gram_length:
                ngram = " ".join(txtfile[word_num - gram_length:word_num+1])
                if ngram not in ngrams:
                    ngrams[ngram] = 0
                ngrams[ngram] +=1
    return ngrams

ngrams = count_ngrams(ngrams)

sorted_ngrams = sorted(ngrams.items(), key=itemgetter(1), reverse=True)

def ask_ngrams():
    answer = input("How many of the top n-grams do you want to see?")
    return answer

number_of_grams = int(ask_ngrams())
if number_of_grams > len(sorted_ngrams):
    print("I'm sorry, that number is too high.")
    number_of_grams = int(ask_ngrams())
    
print(f"The top 10 n-grams are:\n{sorted_ngrams:[:number_of_grams]}")
