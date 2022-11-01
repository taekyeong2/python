'''
filename : baseball.py
숫자구하는게임
2일차 baseball 이랑 비교

'''
#컴퓨터가 난수 3개
from random import randint

#함수
def cnt_strike(c1,c2,c3,n1,n2,n3):  #-> 여섯개값으로 스트라이크 계산
    s= 0
    if c1 == n1:
        s += 1

    if c2 == n2:
        s += 1

    if c3 == n3:
        s += 1
    return s

def cnt_ball(c1,c2,c3,n1,n2,n3): # -> 매개변수
    b=0
    if c1 == n2 or c1 == n3:
        b += 1

    if c2 == n1 or c2 == n3:
        b += 1

    if c3 == n1 or c3 == n2:
        b += 1
    return b #->리턴값

def user_input():
    n1,n2,n3 = input().strip().split(' ')

    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    return n1, n2, n3  #자바스크립트랑 달리 3개 리턴 동시 가능 (원래는 값 1개만 가능)


while True:

    c1 = randint(1,9)
    while True:
        c2 = randint(1,9)
        if c1 != c2:
            break
    while True:
        c3 = randint(1,9)
        if c1 != c3 and c2 != c3:
            break
    print(c1, c2, c3)

    cnt = 0 #게임 시도횟수 
    s= 0
    #숫자 3개 맞췄거나, 시도 횟수가 다 되면 빠져나김
    while s < 3 and cnt < 5: 
        cnt += 1

        #게이머가 값 입력
        n1,n2,n3 = user_input()

        #스트라이크 수 계산
        s = cnt_strike(c1,c2,c3,n1,n2,n3)  #-> 여섯개값으로 스트라이크 계산

        # 볼 갯수 계산
        b = cnt_ball(c1,c2,c3,n1,n2,n3)
        
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

    exitYn = input("게임을 계속 할까요?(y/n): ")
    if exitYn in ['N','n']:
        break


