import pandas as pd
import numpy as np
from os import walk
from operator import itemgetter
import os
import BuildTfMatrix as tf
from nltk.tokenize import RegexpTokenizer




dict={}
score={}

def AddQueryToDictionary(dict,word,docid):
    if not word in dict:
        dict[word]={}
        dict[word][docid]=1
    elif docid not in dict[word]:
        dict[word][docid]=1
    else:
        x = dict[word][docid]
        x += 1
        dict[word][docid]= x
    return dict
for dirpath, dirnames, filesname in walk(r'ShortStories'):
    print()

def Calculate_Tf_IDf(df1):
    for x in df1:
        if(x!='idf' and x!='tf-idf'):
            new='tf-idf'+str(x)
            df1[new]=df1[x]*df1['idf']


def CalculateScore(df):
    magQ = np.sqrt(df['tf-idfq'].dot(df['tf-idfq']))
    i=1
    while (i<51):
        t='tf-idf'+str(i)
        mag=np.sqrt(df[t].dot(df[t]))
        s=sum(df[t]*df['tf-idfq'])
        s=s/(mag*magQ)
        if(s>=0.005):
            score[i]=s
        i+=1
def Process(dict):
    array = []
    term = []

    # All the files in i,e the column names
    files = []
    f = 1
    for i in filesname:
        files.append(f)
        f += 1
    files.append('q')
    files.append('idf')

    # Rows are the terms array has the data of each row from dictionary
    for x in dict:
        array.append(dict[x])
        term.append(x)

    df = pd.DataFrame(array, index=term, columns=files)
    df = df.replace(np.nan, 0)
    df.sort_index(inplace=True)
    Calculate_Tf_IDf(df)
    CalculateScore(df)
    s= sorted(score.items(), key=itemgetter(1),reverse=True)

    return s
def main(query):

    if not os.path.isfile('dictionary.txt'):
        tf.BuildDictionary()
    tokenizer = RegexpTokenizer(r'\w+')
    dictionary = open('dictionary.txt', 'r')
    dict = eval(dictionary.read())
    dictionary.close()

    phrase = tokenizer.tokenize(query)
    for x in phrase:
       dict=AddQueryToDictionary(dict,x, 'q')

    score=Process(dict)
    return score
