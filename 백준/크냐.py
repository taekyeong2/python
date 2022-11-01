'''
큰지안큰지
'''
'''
매개변수 : 숫자 2개
리턴값 ; yes no 0
'''

from unittest import result


def compare(a,b):
    result = 0
    if a == 0 and b == 0:    #0 0 이면 나가야하니까 먼저 입력 (순서)
        result = 0       # 함수에서 끝내는건리턴.
    if a > b:
        result = "Yes"
    else:                  # 첫 번째 수가 두 번째 수보다 크면 Yes를/ 아니면 No를 한 줄에 하나씩 출력한다.(else)
        result = "No"
    return result
    
        
#반복문
while True: 

    #두 수 입력
    a,b = input().split(' ')
    a = int(a)
    b = int(b)

    # 함수 호출: #두수가 0이면 종료 #크면 ㅇ #아니면 ㄴ
    result = compare(a,b)
    if result == 0:
        break            # 함수에서 보다 원래 프로그램에서 끝내는 것이 맞음
    else :
        print(result)