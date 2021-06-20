sentense_s = "English = 89, Science = 90, Math = 92, History = 80."

#각 과목당 점수를 ", "를 기준으로 나눈다.
each_subject = sentense_s.split(", ")

#과목과 점수를 split(" = ")로 나눈 후 각 리스트에 저장한다. 
subject_list = []
score_list = []
for i in range(len(each_subject)):
    subject, sc = each_subject[i].split(" = ")
    #마지막 History = 80. 에서 둘로 나눴을 때 80. 으로 나누어지므로 뒤에 "."을 없애야 한다.
    list_sc = []
    list_sc = list(sc)
    #점수를 sc로 할당하고 이를 list함수를 이용하여 쪼갠다.
    #마지막 인덱스 값이 "."라면 이를 remove(".")로 없애고 다시 조합한다. 그러면 "8", "0", "."값이 "80"으로 바뀌게 된다.
    if list_sc[len(list_sc) - 1] != ".":
        sc = "".join(list_sc)
    else:
        list_sc = list(sc)
        list_sc.remove(".")
        sc = "".join(list_sc)
    score = int(sc)
    subject_list.append(subject)
    score_list.append(score)

#출력
print("총점 : ", sum(score_list))
print("평균점수 : ", sum(score_list) / len(subject_list))
