'''
점수 3개 입력받아서 
합계를 구하는 프로그램
# 수도 코드
'''
'''
#입력
s = input("점수입력: ")  # 90 80 30
#문자를 자르기
kor,eng,mat = s.split(" ")  # 이건 파이썬에서만 가능
# 정수형 변환
kor = int(kor)
eng = int(eng)
mat = int(mat)
#합계
total = kor + eng + mat
#출력
# print(total) 
#국어: 영어: 수학: 합계:
# print("국어:{:5d} 영어:{} 수학:{} \n합계는 {}입니다.".format(kor, eng, mat, total))
print(f"국어:{kor} 영어:{eng} 수학:{mat} \n합계는 {total}입니다.")
'''


kor,eng,mat = input().strip().split(" ") 
#앞뒤에 여백이 있었을때 나는 오류 방지(공백 기준으로 잘라서 배열 넣으니까 - 변수가 더 많아질수있음.)
kor = int(kor)
eng = int(eng)
mat = int(mat)
total = kor + eng + mat
print(f"국어:{kor} 영어:{eng} 수학:{mat} \n합계는 {total}입니다.")
