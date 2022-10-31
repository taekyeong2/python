'''
숫자를 임력받아서 부호를 확인하는 프로그램
'''
'''
#입력
a = input()
#정수변환
a = int(a)  #자바는 변수 이렇게 중복같은거 못씀 달라야함
#양수인지 검사  / 파이썬은 자바랑 달리 비교하려면 타입이 같아야함
if a > 0:
    print("양수")
#음수인지 검사
if a < 0:
    print("음수")
#0인지 검사
if a == 0:
    print("0")
'''

a = input()
a = int(a)  
if a > 0:
    print("양수")
elif a < 0:
    print("음수")
else :
    print("0")