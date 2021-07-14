hex = int(input("입력할 숫자의 진수를 입력하세요(2진, 10진, 16진수) : "))
num = input("숫자를 입력해주세요 : ")
change_hex = int(input("바꿀 숫자의 진수를 입력해주세요 : "))

hex_2 = []
def change_10_for_2(a):
    num_a = int(a)
    if num_a != 0:
        hex_2_num = num_a % 2
        hex_2_number = str(hex_2_num)
        hex_2.append(hex_2_number)
        return change_10_for_2(a / 2)
    else:
        hex_2.append("")

def change_2_for_10(a):
    num_sum = []
    tex_a = str(a)
    for i in range(len(tex_a)):
        num = int(tex_a[i]) * 2**(len(tex_a) - i - 1)
        num_sum.append(num)
    return sum(num_sum)

def change_16_for_2(a):
    num_2 = []
    tex_a = str(a)
    for i in range(len(tex_a)):
        if tex_a[i] == "0":
            num_2.append("0000")
        elif tex_a[i] == "1":
            num_2.append("0001")
        elif tex_a[i] == "2":
            num_2.append("0010")
        elif tex_a[i] == "3":
            num_2.append("0011")
        elif tex_a[i] == "4":
            num_2.append("0100")
        elif tex_a[i] == "5":
            num_2.append("0101")
        elif tex_a[i] == "6":
            num_2.append("0110")
        elif tex_a[i] == "7":
            num_2.append("0111")
        elif tex_a[i] == "8":
            num_2.append("1000")
        elif tex_a[i] == "9":
            num_2.append("1001")
        elif tex_a[i] == "A":
            num_2.append("1010")
        elif tex_a[i] == "B":
            num_2.append("1011")
        elif tex_a[i] == "C":
            num_2.append("1100")
        elif tex_a[i] == "D":
            num_2.append("1101")
        elif tex_a[i] == "E":
            num_2.append("1110")
        elif tex_a[i] == "F":
            num_2.append("1111")
    return "".join(num_2)

def change_2_for_16(a):
    if len(a) % 4 != 0:
        hex_2_num_list = list(a)
        while len(hex_2_num_list) % 4 != 0:
            hex_2_num_list.insert(0, "0")
        hex_2_num = "".join(hex_2_num_list)
        a = hex_2_num
        return change_2_for_16(a)
    else:
        units_4 = []
        units_4.append(a[0 : 4])
        for b in range(4, len(num), 4):
            units_4.append(a[b : b + 4])
        hex_16_num_list = []
        for c in range(len(units_4)):
            if units_4[c] == "0000":
                hex_16_num_list.append("0")
            elif units_4[c] == "0001":
                hex_16_num_list.append("1")
            elif units_4[c] == "0010":
                hex_16_num_list.append("2")
            elif units_4[c] == "0011":
                hex_16_num_list.append("3")
            elif units_4[c] == "0100":
                hex_16_num_list.append("4")
            elif units_4[c] == "0101":
                hex_16_num_list.append("5")
            elif units_4[c] == "0110":
                hex_16_num_list.append("6")
            elif units_4[c] == "0111":
                hex_16_num_list.append("7")
            elif units_4[c] == "1000":
                hex_16_num_list.append("8")
            elif units_4[c] == "1001":
                hex_16_num_list.append("9")
            elif units_4[c] == "1010":
                hex_16_num_list.append("A")
            elif units_4[c] == "1011":
                hex_16_num_list.append("B")
            elif units_4[c] == "1100":
                hex_16_num_list.append("C")
            elif units_4[c] == "1101":
                hex_16_num_list.append("D")
            elif units_4[c] == "1110":
                hex_16_num_list.append("E")
            elif units_4[c] == "1111":
                hex_16_num_list.append("F")
        hex_16_num = "".join(hex_16_num_list)
    return hex_16_num

hex_16 = []
def change_10_for_16(a):
    hex_16 = []
    num_a = int(a)
    if num_a != 0:
        hex_16_num = num_a % 16
        if 0 <= hex_16_num <= 9:
            num_str = str(hex_16_num)
            hex_16.append(num_str)
        elif hex_16_num == 10:
            hex_16.append("A")
        elif hex_16_num == 11:
            hex_16.append("B")
        elif hex_16_num == 12:
            hex_16.append("C")
        elif hex_16_num == 13:
            hex_16.append("D")
        elif hex_16_num == 14:
            hex_16.append("E")
        elif hex_16_num == 15:
            hex_16.append("F")
        return change_10_for_16(a / 16)
    else:
        hex_16.append("")
    hex_16_num = "".join(hex_16)
    return hex_16_num

def change_16_for_10(a):
    hex_16_num = 0
    for i in range(len(a)):
        if a[i] == "0":
            hex_16_num += 0 * 16 ** (len(a) - i - 1)
        elif a[i] == "1":
            hex_16_num += 1 * 16 ** (len(a) - i - 1)
        elif a[i] == "2":
            hex_16_num += 2 * 16 ** (len(a) - i - 1)
        elif a[i] == "3":
            hex_16_num += 3 * 16 ** (len(a) - i - 1)
        elif a[i] == "4":
            hex_16_num += 4 * 16 ** (len(a) - i - 1)
        elif a[i] == "5":
            hex_16_num += 5 * 16 ** (len(a) - i - 1)
        elif a[i] == "6":
            hex_16_num += 6 * 16 ** (len(a) - i - 1)
        elif a[i] == "7":
            hex_16_num += 7 * 16 ** (len(a) - i - 1)
        elif a[i] == "8":
            hex_16_num += 8 * 16 ** (len(a) - i - 1)
        elif a[i] == "9":
            hex_16_num += 9 * 16 ** (len(a) - i - 1)
        elif a[i] == "A":
            hex_16_num += 10 * 16 ** (len(a) - i - 1)
        elif a[i] == "B":
            hex_16_num += 11 * 16 ** (len(a) - i - 1)
        elif a[i] == "C":
            hex_16_num += 12 * 16 ** (len(a) - i - 1)
        elif a[i] == "D":
            hex_16_num += 13 * 16 ** (len(a) - i - 1)
        elif a[i] == "E":
            hex_16_num += 14 * 16 ** (len(a) - i - 1)
        elif a[i] == "F":
            hex_16_num += 15 * 16 ** (len(a) - i - 1)
    return hex_16_num

def flip(some_list):
    if len(some_list) < 2:
        return some_list
    else:
        return flip(some_list[1:]) + some_list[:1]

if hex == 10 and change_hex == 2:
    number = int(num)
    change_10_for_2(number)
    print(num, ">>>" ,"".join(flip(hex_2)))

if hex == 2 and change_hex == 10:
    number = int(num)
    print(num, ">>>", change_2_for_10(number))

if hex == 16 and change_hex == 2:
    print(num, ">>>", change_16_for_2(num))

if hex == 2 and change_hex == 16:
    print(num, ">>>", change_2_for_16(num))

if hex == 10 and change_hex == 16:
    print(num, ">>>", change_10_for_16(num))

if hex == 16 and change_hex == 10:
    print(num, ">>>", change_16_for_10(num))
