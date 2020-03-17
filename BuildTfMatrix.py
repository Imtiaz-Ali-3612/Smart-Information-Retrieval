import math
import pandas as pd
import numpy as np
from os import walk
from nltk.tokenize import RegexpTokenizer

StopWords=["a","is", "the", "of", "all" ,"and", "to", "can", "be", "as","once","for","at","am","are","has","have","had","up","his","her","in","on","no","we","do"]

for dirpath, dirnames, filesname in walk(r'ShortStories'):
    print()
PositionalIndex={}
def index(word,docid):
    if not word in PositionalIndex:
        PositionalIndex[word]={}
        PositionalIndex[word][docid]=1
    elif docid not in PositionalIndex[word]:
        PositionalIndex[word][docid]=1
    else:
        x = PositionalIndex[word][docid]
        x += 1
        PositionalIndex[word][docid]= x

def Calculate_IDF(N):
    for x in PositionalIndex:
        if 'q' in PositionalIndex[x]:
           df=len(PositionalIndex[x])-1
        else:
            df=len(PositionalIndex[x])
        PositionalIndex[x]['idf']=math.log10(N/df)

def BuildDictionary():
    tokenizer = RegexpTokenizer(r'\w+')

    for file in filesname:
        f = open(dirpath + "/" + file, "r")
        phrase = f.read()
        f.close()
        file = file.replace('.txt', '')
        phrase = phrase.casefold()
        phrase = tokenizer.tokenize(phrase)
        for x in phrase:
            if (x not in StopWords):
                index(x, int(file))


    Calculate_IDF(50)
    array = []  # array of Dictionary postings

    words = []  # array of terms

    dictionary = open('dictionary.txt', 'w+')
    dictionary.write(str(PositionalIndex))
    dictionary.close()

