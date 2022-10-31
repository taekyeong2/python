'''
리스트 조회
'''

members = [
    {'name': '김태경', 'age': 28, 'addr': '대구시'}, 
    {'name': '김꼬미', 'age': 1, 'addr': '대구시'}, 
    {'name': '김보미', 'age': 1, 'addr': '대구시'}
    ]

    # 전체출력
# for member in members: #member은 객체를 나타낸다.
#     if member['age'] == '28':
#         print(f'{member["name"]}\t{member["addr"]}')

# members[0]["name"]

# for member in members:
#     age = int(input("검색할나이입력: "))
#     if member["age"] == age:
#         print(f'{member["name"]}\t{member["addr"]}')

name = input("이름입력: ") #-> 한번만 이름 검색 하려면 빼줘야함
for member in members:
    # if member["name"].find(name) >=0:  #->indexOf 와 같다.
    if name in member["name"]: #->위에거랑 같음.
        print(f'{member["name"]}\t{member["addr"]}')
        #삭제 
