'''
리스트 다루기
'''

# list_a=['hello',10,True]
# print(list_a[1])
# print(list_a[0][0])

list = []
for i in range(3):
    info={}
    info["name"]=input("이름입력: ")
    info["age"]=input("나이입력: ")
    info["addr"]=input("주소입력: ")
    
    #리스트에 추가
    list.append(info)

for member in list:
    print(f'{member["name"]}\t{member["age"]}')

