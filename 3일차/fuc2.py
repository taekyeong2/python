'''
지역변수
'''

# #함수 선언
# def mysum():
#     total = 0
#     for i in range(11): # 0부터 10까지 반복 / i ->반복변수(ijk많이씀.)
#         total += i

#     print(total)




# #함수호출
# mysum()

#========================================================

#함수 선언
def mysum(n):  # 호출할때의 변수를 받아주기 위한 ㅂ변수.(매개변수)
    total = 0
    for i in range(n+1): # 0부터 10까지 반복 / i ->반복변수(ijk많이씀.)
        total += i

    # print(total)  # 내가 결과를 마음대로 출력하고 싶다.
    return total # 리턴값을 넘겨주는것.(호출 좌측(t1)에서 리턴값을 받음.) / 원래 함수에서 기본으로 리턴있음(함수끝나고 다시 호출한 곳으로 돌아가는것.) 


# print(total) # 여기선 인지 못함, total은 함수 안에서만 존재. (지역변수)/ 

#함수호출
num = int(input("입력: "))
t1 = mysum(num)  # t1 -> 넘겨받은 리턴값
print('합계는',t1)

num = int(input("입력: "))
t1 = mysum(num)
print('합계는',t1,'입니다.')
