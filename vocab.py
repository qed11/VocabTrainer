# coding = utf8
from random import randint

def ask(key,vocab):
    answer = vocab[key]
    counter = 2
    print(key)
    while (counter>=0):
        user = input('Enter word:')
        if user == 'Q':
            return False
        elif user == 'A':
            for i in answer:
                print(i)
            return True
        elif user in answer:
            print("Correct")
            if len(answer)>1:
                print('These words have the same meaning:')
                for i in answer:
                    if answer != i:
                        print(i)
            return True
        print("Wrong answer. You have",counter,'tries left')
        counter -= 1
    print("The correct answer is: ",end='')
    for i in answer:
        if i.index!=len(answer)-1:
            print(i,end=',')
        else:
            print(i)
    return True

def trainer(vocab):
    chnKey = list()
    cond = True
    print("Press Q to end")
    for i in vocab:
        chnKey.append(i)
    while cond:
        index = randint(0,len(chnKey)-1)
        cond = ask(chnKey[index],vocab)
        print('----------------------------')

if __name__=='__main__':
    lines = open('vocabularyList.txt',encoding='utf8').readlines()
    vocabBook = dict()
    for i in range(len(lines)):
        lines[i]=lines[i].replace('\n','')
        eng, chn= lines[i].split(' ')
        if chn in vocabBook:
            vocabBook[chn].append(eng)
        else:
            vocabBook[chn] = [eng]
    trainer(vocabBook)  

    
