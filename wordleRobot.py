import numpy as np
import re
from wordfreq import word_frequency

letters=['e', 's', 'i', 'a', 'r', 'n', 't', 'o', 'l', 'c', 'd', 'u', 'g', 'p', 'm',
'k', 'h', 'b', 'y', 'f', 'v', 'w', 'z', 'x', 'q', 'j']

with open("/usr/share/dict/words") as f:   
    words=[word for word in [w.strip().lower() 
                for w in f.readlines()] if (len(word) == 5 )] 
         
def letterFrequency(words,letters):         
    listLetterFreq=[]
    for w in words: 
        score=0
        for c in w:
            if c in letters:
                score += letters.index(c) 
            else:
                score += 100
        listLetterFreq.append(score)
    return listLetterFreq

def positionFrequency(words,letters): 
    repetitive=[]
    for i in range(0,5):
        dic={letters[i]: 0 for i in range(0, len(letters))}
        for w in words:
            if w[i] in dic:
                dic.update({w[i]: dic[w[i]]+1})
        repetitive.append({k: v for k, v in
                sorted(dic.items(),reverse=1, key=lambda item: item[1])})
    return repetitive 

def Decision(Data,pFreq):
    wFreqList=[]
    sitem=('',0)
    if len(Data)<4:
        rang=1
    else:
        rang=len(Data)//4
    for d in Data:
        wFreqList.append(d[2])
    wFreqList.sort(reverse=True)   
    for i in wFreqList[:rang]:
        for d in Data:
            if (d[2]==i and d[1]>sitem[1]):
                sitem=(d[0],d[1])
    return sitem[0]
lFreq=letterFrequency(words,letters)
wFreq=[word_frequency(w,lang='en') for w in words]
Data=[(words[i],lFreq[i],wFreq[i]) for i in range (0,len(words))]
pFreq=positionFrequency(words,letters)

newData=[]
for t in range(0,6):
    if t != 0:
        #print()
        #print(Data)
        #print(Decision(Data,pFreq))
        #word=input("\n: ")
        word=Decision(Data,pFreq)
    else:
        word="anise\n"

    print(word) # simple output
    feedBack=input("Enter Feedback(-,*,#): ") # simple input 

    for step in range(0,5): #FILTER
        if feedBack[step] == '-':
            for d in Data:
                if not(word[step] in d[0]):
                    newData.append(d)
        elif feedBack[step] == '#': 
            for d in Data: 
                if word[step] in d[0] and d[0][step]!=word[step]: 
                    newData.append(d)        
        elif feedBack[step] == '*':
            for d in Data:
                if d[0][step]==word[step]:
                    newData.append(d)
        Data=newData
        newData=[]