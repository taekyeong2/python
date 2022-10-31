'''
리스트에 요소 추가 : insert, appedn 함수
'''

#키보드로부터 숫자 5개 입력받아서 리스트에 저장

arr = []
#반복5번 cf)자바스 -> for(i=1; i<=5 ; i++)
for i in range(5) :
    #키보드입력
    a = input()
    #리스트에 추가
    arr.append(a)

#리스트 출력
print(arr)


# for : 반복횟수
# while : 반복횟수 모름, 조건식