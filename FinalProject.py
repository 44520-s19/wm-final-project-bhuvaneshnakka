# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 13:06:24 2019

@author: s534846
"""

import pickle

with open('article_text.pkl','rb') as f:
    article_text = pickle.load(f)
 
from nltk.tokenize import word_tokenize, sent_tokenize

sentences =sent_tokenize(article_text)
tokens =[word_tokenize(sent) for sent in sentences]

print(tokens)

def term_freq(term,doc):
    all_lower =[token.lower() for token in doc]
    all_lower.count(term.lower())
    
def  inv_doc_freq(term, docs):
    count =0
    for doc in docs:
        all_lower =[token.lower() for token in doc]
        if term.lower() in all_lower:
            count+= 1 
        if count==0:
            return 1
        return 1 + log(len(docs)/count)
    
def tf_idf(term,doc,docs):
    return term_freq(term,doc)*inv_doc_frq(term,docs)
print('the:', tf_idf('the',tokens[0],tokens))
print('raspberry:',tf_idf('raspberry',tokens[0],tokens))

words =set()
for sent in tokens:
    words =  words.union(set([toke.lower() for token in sent]))
scores =dict()
for word in words:
    scores[word] =total_tfidf(word,tokens)
 best_word(max(words,lambda x: score[x]))
print('word with highest score is', best_word,)   
print(scores)        
    
    
    
    