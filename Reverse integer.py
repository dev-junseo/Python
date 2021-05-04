num = input("정수를 입력하세요 : ")
def flip(num):
    if len(num) < 2:
        return num
    else:
        return flip(num[1:]) + num[:1]
while True:
    if num == flip(num):
        print("%s은(는) 거꾸로 정수입니다." %(num))
        num = input("정수를 입력하세요 : ")
    elif num != flip(num):
        print("%s은(는) 거꾸로 정수가 아닙니다." %(num))
        num = input("정수를 입력하세요 : ")
    if num == "-99":
        print("프로그램을 종료합니다.")
        break
