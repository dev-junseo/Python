well_deep = 30
snail_location = 0
date = 0

while well_deep > snail_location:
    snail_location += 7
    if date > 0:
        snail_location -= 5
    print("day %d : 달팽이의 위치 : %d 미터" %(date + 1, snail_location))
    if well_deep < snail_location:
        print("축하합니다. 우물을 탈출하였습니다.")
        print("우물을 탈출하는데 걸린 날은 %d일 입니다." %(date + 1))
    date += 1
