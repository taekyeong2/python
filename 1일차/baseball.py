'''
filename : baseball.py
숫자구하는게임
'''
#컴퓨터가 난수 3개
from random import randint

c1 = randint(1,9)
c2 = randint(1,9)
c3 = randint(1,9)
# print(c1, c2, c3)

cnt = 0 #게임 시도횟수 
s=0
while s < 3 and cnt < 5: 
    cnt += 1
    #게이머가 값 입력
    n1,n2,n3 = input().strip().split(' ')

    #정수형 변환
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)

    s=0 # 리셋 - 점수가 누적되니까 초기화 되어야함
    b=0
    #스트라이크 수 계산
    if c1 == n1:
        s += 1

    if c2 == n2:
        s += 1

    if c3 == n3:
        s += 1

    # 볼 갯수 계산
    if c1 == n2 or c1 == n3:
        b += 1

    if c2 == n1 or c2 == n3:
        b += 1

    if c3 == n1 or c3 == n2:
        b += 1
    print(f'스트라이크:{s} ball:{b}')

#스타라이크 3이면 축하. ->  4번이면 보통 시도횟수 3번만에 맞추면 천재 

if s == 3:
    print("축하합니다")
    if cnt <= 3:
        print("천재입니다")
    elif cnt == 4:
        print("우수합니다")
    else:
        print("보통입니다")
else:
    print("게임오버")

print("게임종료")

