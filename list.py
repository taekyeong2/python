'''
list == array
배열에 요소를 추가, 삭제, 조화 , 변경
'''

arr = ['김','이','박','옹']

# 마지막에 최씨 추가
arr.append('최')

# 맨처음 강씨 추가'
arr.insert(0,'강')

#김씨 삭제 -ㅁ 명ㅇ령어
del arr[1]

# 박 삭제 - 함수
arr.remove('박')

print(arr)