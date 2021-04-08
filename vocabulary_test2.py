voca = {}

voca['교회'] = 'church'
voca['사과'] = 'apple'
voca['자전거'] = 'bicycle'
voca['지갑'] = 'wallet'
voca['절'] = 'tample'
voca['비누'] = 'soap'
voca['고양이'] = 'cat'

from random import randint
voca_keys = list(voca.keys())
while True:
    index = randint(0, len(voca_keys) - 1)
    korean_word = voca_keys[index]
    english_word = voca[korean_word]
    question = input("%s: " %(korean_word))
    if question == "q":
        break
    if question == english_word:
        print("맞았습니다!\n")
    elif question != english_word:
        print("틀렸습니다. 정답은 %s입니다.\n" %(english_word))

    