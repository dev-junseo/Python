from random import randint
numbers = []
while len(numbers) < 3:
    new_number = randint(0, 9)
    while new_number in numbers:
        new_number = randint(0, 9)
    numbers.append(new_number)
x = numbers[0]
y = numbers[1]
z = numbers[2]
print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
strike = 0
ball = 0
count = 0
while strike < 3:
    print("세 수를 하나씩 차례대로 입력하세요.")
    a = int(input("첫번째 수를 입력하세요: "))
    while a >= 10:
        print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
        a = int(input("첫번째 수를 입력하세요: "))
    if x == a:
        strike = strike + 1
    elif (y == a) or (z == a):
        ball = ball + 1
    b = int(input("두번째 수를 입력하세요: "))
    while b >= 10:
        print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
        b = int(input("첫번째 수를 입력하세요: "))
    if b == y:
        strike += 1
    elif (b == x) or (b == z):
        ball += 1
    c = int(input("세번째 수를 입력하세요: "))
    while c >= 10:
        print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
        c = int(input("세번째 수를 입력하세요: "))
    if c == z:
        strike += 1
    elif (x == c) or (y == c):
        ball += 1
    print("strike : %d \n ball : %d" %(strike, ball))
    if strike < 3:
        strike = 0
        ball = 0
        count += 1
    if strike == 3:
        print("축하합니다. %d번 만에 맞췄습니다." %(count))