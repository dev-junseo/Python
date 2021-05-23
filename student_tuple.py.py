student_tuple = [("211101", "강이안", "010-123-1111"), ("211102", "박동민", "010-123-2222"), ("211103", "김수정", "010-123-3333")]

#학번 : 이름 딕셔너리 만들기
student_num_info = {}
for i in range(len(student_tuple)):
    student_info_list = student_tuple[i]         #튜플 하나의 인덱스를 다시 하나의 리스트로 만든다.
    student_num_info[student_info_list[0]] = student_info_list[1]      #만든 리스트의 인덱스로 딕셔너리를 만든다.

#출력
for num, name in student_num_info.items():
    print(num, " : ", name)

#학번 : 전화번호 딕셔너리 만들기
student_phone_num = {}
for j in range(len(student_tuple)):
    student_p_list = student_tuple[i]      #같은 방법으로 튜플 하나의 인덱스를 다시 하나의 리스트로 만든 후 이를 student_phone_num 딕셔너리로 만든다.
    student_phone_num[student_p_list[0]] = student_p_list[2]

student_ID = input("학번을 입력하세요 : ")
print("%s 학생은 %s이며, 전화번호는 %s입니다." %(student_ID, student_num_info[student_ID], student_phone_num[student_ID]))