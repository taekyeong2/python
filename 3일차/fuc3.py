'''
전역변수
'''

total =0

def mysum():
    total =0 
    for i in range(11):
        total += i

mysum()
print(total)

#==============================================

# 전역변수
total =0

def mysum():
    global total  #전역변수 토탈 쓰겠다고 선언.
    for i in range(11):
        total += i

mysum()
print(total)  #함수안 토탈과 바깥 토탈과는 다르다.