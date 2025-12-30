# 실습문제 20

# 입력 = int(input())
# sum = 0 

# for i in range((입력)):
#     sum += (i + 1)
# print(sum)

# 실습문제 21

# n = int(input("첫번째"))
# m = int(input("두번째"))
# k = 0

# for i in range(n,m + 1):
#     k += i
# print(k)

# 실습문제 22

# for i in range(1,11,2):
#     print(i)

# i = 1
# while i < 11:
#     print(i)
#     i += 2

# 실습문제 23

구구단 = int(input("몇 단을 출력할까요?"))

for i in range(1,10):
    # print(구구단,"*",i+1,"=",구구단*(i+1))
    print(f'{구구단}*{i}={구구단}*{i}')