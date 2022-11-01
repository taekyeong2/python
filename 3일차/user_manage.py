'''
user manage
메뉴선택
리터값: 입력된 메뉴번호
'''
from turtle import clear


def menu_select():
    print("1.추가, 2.삭제, 3.조회, 4.전체조회, 5.전체삭제, 6.종료")
    no = int(input("메뉴선택: "))
    return no

def user_insert():
    info={}
    info["userno"]=int(input('번호입력: ')) 
    info["username"]=input('이름입력: ')
    info["salary"]=int(input('급여입력: '))
    return info

def user_delet(userno):
    idx = 0
    for obj in users:
        if obj["userno"] == userno:
            del users[idx]
            break
        idx += 1 

def user_select(userno):
    for idx in range(len(users)):
        if userno == users[idx]['userno']:
            print(f'{users[idx]["username"]}\t{users[idx]["salary"]}')

def user_selAll():
    for i in users:
            print(f'{i["username"]}\t{i["salary"]}')

def user_clear():
    users.clear()

users = [    #전역변수
    {'userno':100, 'username': 'user1', 'salary':2000},
    {'userno':101, 'username': 'user2', 'salary':1000},
    {'userno':102, 'username': 'user3', 'salary':1500}
]

while True:

    #메뉴선택
    no = menu_select()  #변수가 필요하다면 리턴값필요.

    if no == 1:
        print("추가: ")

        info = user_insert()
        users.append(info)

    elif no == 2:
        userno = int(input("삭제할 번호 입력: "))
        user_delet(userno)   #삭제할 번호 입력 받아서 함수로 넘겨줄것임. -> userno를 함수의 매개변수로

    elif no == 3:
        userno = int(input("조회할 번호 입력: "))
        user_select(userno)

    elif no == 4:
        print("전체조회")
        user_selAll()

    elif no == 5:
        user_clear()

    elif no == 6:
        break
print("the end")
