while True:
    order = input("명령 내려주세요")
    if order == "go":
        print("계속 진행 합니다")
    elif order == "stop":
        print("종료합니다")
        break
    else:
        print("잘못 입력했습니다")