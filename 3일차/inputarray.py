'''
input arrary
'''

no = input()
arr = input().split()  # int 안해도 문자와 문자끼리 가능
cnt = 0
# arr의 리스트의,요소값과 no가 같으면 cnt 증가
for obj in arr:
    if obj == no:
        cnt += 1

print(cnt)