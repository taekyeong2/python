'''
매개변수와 리턴이 없는 함수
'''

# #함수 선언
# def print_3_hello():
#     print(안녕)
#     print(안녕)
#     print(안녕)


# #함수 호출
# print_3_hello()
# print()
# print_3_hello()


#함수 선언
# def print_3_hello(greet):
#     print(greet)
#     print(greet)
#     print(greet)

def print_3_hello(greet, n=2): #(변수, 반복횟수n) -> 매개변수
    for i in range(n):  #i -> 지역변수,local(함수 밖에서 없어짐)
        print(greet, end=" ") #->기본 \n 없이 옆으로 출력
    
#함수 호출
# print_3_hello("안녕", 2) # 자바스크립트에서는 매개변수와 달라도 오류가 안남
# print()
# print_3_hello("hi", 4)

g = "안녕하세요"
n = 10
print_3_hello(g, n) 
print()
print_3_hello(n=3, greet="hi") #이렇게 하면 인수 순서다르게 해도됨./파이썬만 가능


#https://docs.python.org/3.11/library/functions.html -> 파이썬 기본 제공 함수

print('a','b','c',sep='-')
print('a','b','c',end=' ')
input()