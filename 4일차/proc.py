#학생의 성적을 계산하는 프로그램
std = [
    {'mat':50, 'eng':90},
    {'mat':70, 'eng':80},
    {'mat':80, 'eng':60}
]

#수학성적의 합
matSum = 0
for score in std:
    matSum += score['mat']
print(matSum)