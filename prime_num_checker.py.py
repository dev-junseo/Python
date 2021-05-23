num = int(input("소수 검사를 할 정수를 입력하시오 : "))
num_list = []
def make_num_list(number):
    if number == 2:
        num_list.append(number)
        return num_list
    elif number > 2:
        for i in range(2, number):
            num_list.append(i)
        return num_list

count = 0
make_num_list(num)
for i in range(len(num_list) - 1):
    num_1 = num_list[i]
    if num % num_1 == 0:
        count += 1
if count == 0:
    print("소수인가요? : True")
elif count >= 1:
    print("소수인가요? : False")

