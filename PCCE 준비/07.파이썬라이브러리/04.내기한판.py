import turtle as t
import random
import time

# 가로 800, 새로 800 배경변경
t.setup(width=800, height=800)
t.shape("turtle")
t.color('orange')
t.bgcolor('steelblue')

# 중앙선 만들기
t.goto(0,400)
t.goto(0,-400)
t.goto(0,-0)

# 속도 변경
t.speed(1)

# 펜 올리기
t.penup()

for i in range(10):
    t.forward(random.randint(-50,50))
    time.sleep(1)

if t.xcor() > 0:
    t.write("거북이가 오른쪽으로 감", font=("Arial",16))
elif t.xcor() < 0:
    t.write("거북이가 왼쪽으로 감", font=("Arial",16))
#화면 클릭 되었을 때 종료
t.exitonclick()