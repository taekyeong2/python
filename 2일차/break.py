'''
break (p244)
'''

# while True:
#     no = int(input("번호: "))
#     if no == 0:
#         break
# print("the end")

users = [ 
    {'userno':100, 'username': 'user1', 'salary':2000},
    {'userno':101, 'username': 'user2', 'salary':1000},
    {'userno':102, 'username': 'user3', 'salary':1500}
]
while True:
    print("1.추가, 2.삭제, 3.조회, 4.전체조회, 5.종료")
    no = int(input("메뉴선택: "))
    if no == 1:
        print("추가: ")
        info={}
        info["userno"]=int(input('번호입력: ')) # **** int해야지 숫자로 인식해서 삭제됨
        info["username"]=input('이름입력: ')
        info["salary"]=int(input('급여입력: '))

        users.append(info)
    elif no == 2:
        userno = int(input("삭제할 번호 입력: "))
        # for idx in range(len(users)):
            # if userno == users[idx]['userno']: # 'in'은 string이나 배열일때 사용, 숫자(int)값 비교할땐 == 사용
            #     del users[idx]
            #     break  # 이건 전체 while문에서 빠지는게 아니라 elif안for문에 빠져나오는것
        idx = 0
        for obj in users:
            if obj["userno"] == userno:
                del users[idx]
                break
            idx += 1 #if 충족이안되면 idx값이 1이 더 늘어남 -> 두번째에서 충족이 되면 del user[1] 됨.
    elif no == 3:
        #번호 입력
        userno = int(input("조회할 번호 입력: "))
        #번호 입력받고 해당번호 이름과 급여 출력
        for idx in range(len(users)):
            if userno == users[idx]['userno']:
                print(f'{users[idx]["username"]}\t{users[idx]["salary"]}')
    elif no == 4:
        print("전체조회")
        # username, 급여
        for i in users:
            print(f'{i["username"]}\t{i["salary"]}')
    elif no == 5:
        break
print("the end")
