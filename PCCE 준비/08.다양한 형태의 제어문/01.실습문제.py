# 실습문제 24

구독자수 = int(input("현재 구독자 수"))
시청시간 = int(input("시청시간"))

if (구독자수>=1000)&(시청시간>=4000):
    print("수익 창출 가능")
else:
    print("수익 창출 불가능")

# 실습문제 25

팔굽혀펴기 = int(input("팔굽혀펴기:"))
윗몸일으키기 = int(input("윗몸일으키기:"))
턱걸이 = int(input("턱걸이:"))

if 팔굽혀펴기 >= 30 or 윗몸일으키기 >= 35 or 턱걸이 >= 5:
    print("pass")
else:
    print("fail")

# 실습문제 26

필기시험 = int(input("필기시험 점수를 입력하세요:"))

if 필기시험 >= 80:
    면접 = input("면접결과를 입력하세요:")
    if 면접 == "pass":
        print("최종합격")
    else:
        print("불합격")
else:
    print("불합격")

# 실습문제 27

for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()

# 실습문제 28

for i in range(5,0,-1):  
    for j in range(i):
        print("*", end="")
    print()

for i in range(5):
    for j in range(5-i):
        print("*", end="")
    print()

# 실습문제 29

for i in range(5): # 0 1 2 3 4   
    for j in range(4-i):
        print(" ",end="")
    for j in range((i+1)*2-1):
        print("*",end="")
    print()

# 실습문제 30

while True:
    print("[메뉴를 입력하세요]")
    order = int(input("1.게임시작 2.랭킹보기 3. 게임종료 >>>"))
    if order == 1:
        print("게임을 시작합니다.")
    elif order == 2:
        print("실시간 랭킹")
    elif order == 3:
        print("게임을 종료합니다.")
        break
    else:
        print("다시 입력해주세요.")