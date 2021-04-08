voca_list = open('vocabulary_list.txt', 'r')

for list in voca_list:
    interchange = list.strip().split(": ")
    voca = interchange[1]
    answer = interchange[0]
    test = input("%s: " %(voca))
    if answer == test:
        print("맞았습니다!\n")
    else:
        print("아쉽습니다. 정답은 %s입니다.\n" %(answer))
voca_list.close()
        