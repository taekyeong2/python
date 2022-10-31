'''
리스트 삭제
'''

from re import I


members = [
    {'name': '김태경', 'age': 28, 'addr': '대구시'}, 
    {'name': '김꼬미', 'age': 1, 'addr': '대구시'}, 
    {'name': '김보미', 'age': 1, 'addr': '대구시'}
    ]

name = input("이름입력: ") 
for i in range(len(members)): #-> 배열만큼 반복(3) / i는 인덱스
    if name in members[i]["name"]: 
        print(f'{members[i]["name"]}\t{members[i]["addr"]}')
        del members[i]  # ->하나 빠지면 인덱스값도 하나 줄어들어서 for문 반복 범위에 벗어나서 오류남
        break

print(members)

#for(i=0; i<10; i=i+2) = range(0,10,2) ->0부터 10까지 2씩 올라감 (여기서 10은 포함 노노)