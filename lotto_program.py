from random import randint


# 1~45 사이 무작위 6개의 숫자 뽑기
g_num = []
def generate_numbers():
    while len(g_num) != 6:
        a = randint(1, 45)
        if a not in g_num:
            g_num.append(a)
    return sorted(g_num)
print(generate_numbers())

# 앞에서 뽑은 6개의 숫자와 다른 보너스 숫자를 추가

def draw_winning_numbers():
    number = generate_numbers()
    bonus_number = randint(1, 45)
    while len(number) < 7:
        if bonus_number not in number:
            number.append(bonus_number)
    return number

print(draw_winning_numbers())

# 두 리스트에서 겹치는 번호 개수 리턴
def count_maching_numbers(list1, list2):
    count = 0
    for num in list1:
        if num in list2:
            count += 1
    return count

print(count_maching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_maching_numbers([2, 7, 11, 14, 25, 40], [2, 13, 14]))

# 당첨 금액 리턴
def check(numbers, winning_numbers):
    count = 0
    for num in numbers:
        if num in winning_numbers:
            count += 1
    
    if count == 6:
        return 1000000000
    if count == 5 and winning_numbers[6] in numbers:
        return 50000000
    elif count == 5 and winning_numbers[6] not in numbers:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return "꽝"

print(check(generate_numbers(), draw_winning_numbers()))