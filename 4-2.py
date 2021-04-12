#첫번째 방법
number_1, number_2, number_3 = input("세 정수를 입력하시오 : ").split()
num_1 = int(number_1)
num_2 = int(number_2)
num_3 = int(number_3)
sort = []
sort.append(num_1)
sort.append(num_2)
sort.append(num_3)
sort.sort()
print(sort[2], sort[1], sort[0])

#두번째 방법
number_1, number_2, number_3 = input("세 정수를 입력하시오 : ").split()
num_1 = int(number_1)
num_2 = int(number_2)
num_3 = int(number_3)
# 123 132 213 231 312 321
if num_1 > num_2 > num_3:
    print("%d %d %d" %(num_1, num_2, num_3))
elif num_1 > num_3 > num_2:
    print("%d %d %d" %(num_1, num_3, num_2))
elif num_2 > num_1 > num_3:
    print("%d %d %d" %(num_3, num_1, num_2))
elif num_2 > num_3 > num_1:
    print("%d %d %d" %(num_2, num_3, num_1))
elif num_3 > num_1 > num_2:
    print("%d %d %d" %(num_3, num_1, num_2))
elif num_3 > num_2 > num_1:
    print("%d %d %d" %(num_3, num_2, num_1))
