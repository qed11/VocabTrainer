# coding = utf8
from random import randint

def ask(key,vocab,wrong):
    answer = vocab[key]
    counter = 2
    print(key)
    while (counter>=0):
        user = input('Enter word:')
        if user == 'Q':
            return 0
        elif user == 'A':
            for i in answer:
                print(i)
            wrong.add(key)
            return 2
        elif user in answer:
            print("Correct")
            if len(answer)>1:
                print('These words have the same meaning:')
                for i in answer:
                    if i != user:
                        print(i)
            return 1
        print("Wrong answer. You have",counter,'tries left')
        counter -= 1
    print("The correct answer is: ",end='')
    for i in answer:
        if i.index!=len(answer)-1 and len(answer)!=1:
            print(i,end=',')
        else:
            print(i)
    wrong.add(key)
    return 2

def trainer(vocab):
    chnKey = list()
    wrong = set()
    cond = True
    print("Welcome to <name>. You will be prompted with <language> words. You can press Q to end (very encouraged to)")
    for i in vocab:
        chnKey.append(i)
    while cond != 0:
        index = randint(0,len(chnKey)-1)
        cond = ask(chnKey[index],vocab,wrong)
        print('----------------------------')
        if cond == 2:
            f = open('Improvements.txt','w',encoding = 'utf8')
            for i in wrong:
                f.write(i+'\n')    
            f.close()   

def prepareDic(filename):
    lines = open(filename,encoding='utf8').readlines()
    vocabBook = dict()
    for i in range(len(lines)):
        lines[i]=lines[i].replace('\n','')
        eng, chn= lines[i].split(' ')
        if chn in vocabBook:
            vocabBook[chn].append(eng)
        else:
            vocabBook[chn] = [eng]
    return vocabBook

def correctWrongs(vocab,wrongFilename):
    #using keys from incorrections on the last time
    pass


if __name__ == '__main__':
    vocabBook = prepareDic('vocabularyList.txt')
    #correctWrongs
    trainer(vocabBook)