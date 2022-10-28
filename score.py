'''
점수 3개 입력받아서 
합계를 구하는 프로그램
# 수도 코드
'''
'''
#입력
s = input("점수입력: ")  # 90 80 30
#문자를 자르기
score = s.split(" ")
# 정수형 변환
kor = int(score[0])
eng = int(score[1])
mat = int(score[2])
#합계
total = kor + eng + mat
#출력
print(total)
'''

s = input("점수입력: ") 
score = s.split(" ")
kor = int(score[0])
eng = int(score[1])
mat = int(score[2])
total = kor + eng + mat

#평균
p = total/3
#평균이 90점 이상이면 수 80이상이면 우 70이상이면 미 나머지 양
if p >= 90:
    print("수")
elif p >=80:
    print("우")
elif p >=70:
    print("미")
else :
    print("양")