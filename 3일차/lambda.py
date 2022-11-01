'''
람다
매개변수 함수를 전달하고자 할때 함수선언을 람다식으로 표현
'''

def print_hi():
    print("안녕하세요")

def print_hello():
    print("안녕하세요")

def call_10(func):  #함수의 매개변수가 함수
    for i in range(10):
        func()  # 이때 위의 함수 호출

call_10(print_hello) # 함수 호출 안할거라서 ()안넣음. 그냥 함수에 넘겨줌
# s
#람다식
call_10(lambda  : print("hi"))