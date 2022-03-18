from wordfreq import word_frequency

letters=['e', 's', 'i', 'a', 'r', 'n', 't', 'o', 'l', 'c', 'd', 'u', 'g', 'p', 'm',
'k', 'h', 'b', 'y', 'f', 'v', 'w', 'z', 'x', 'q', 'j']

with open("words") as f:   
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

def positionFrequency(words,letters): #TODO 
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
pFreq=positionFrequency(words,letters) #TODO

if __name__=="__main__": 
    print("Hey! Calm Down, I am here to solve wordle chalnge(*_*).")
    print("="*10)
    print("Just give me a feedback like: ")
    print("=> * : The letter X is in the word and in the correct spot.")
    print("=> # : The letter X is in the word but in the wrong spot.")
    print("=> - : The letter X is not in the word in any spot." )
    print("="*10)

    newData=[]
    for t in range(0,6):
        if t != 0:
            word=Decision(Data,pFreq)
        else:
            print("I think:",end="  ")
            word="anise\n"

        print(word) 
        feedBack=input("Enter its feedback(-,*,#,q=end): ") 
        print("-----")

        if feedBack=='q':
            break
        for step in range(0,5):
            # filter data in this section
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
            
    print("(#_#) SOAL.")