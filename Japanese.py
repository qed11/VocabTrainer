from random import randint

if __name__ == '__main__':
    bowel = ['','k','s','t','n','h','m','g','z','d','b','p']
    vowel = ['a','i','u','e','o']
    state = 1
    while state == 1:
        a = bowel[randint(0,len(bowel)-1)]
        b = vowel[randint(0,4)]
        print(a+b)
        choice = input('Continue?(y/n)')
        if choice == 'n':
            state = 0
        print('-------------------- ')