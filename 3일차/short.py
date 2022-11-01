arr = [1,2,4,10,7]
arr.sort()    # 알아서 배열 정리
print(arr)

arr.sort(reverse=True)    # d역순으로 정리
print(arr)

#-------------------------------------------------------------------

users = [    #전역변수
    {'userno':100, 'username': 'user1', 'salary':2000},
    {'userno':101, 'username': 'user2', 'salary':1000},
    {'userno':102, 'username': 'user3', 'salary':1500}
]

#급여순으로 정리
users.sort(key= lambda item : item['salary'], reverse=True ) #어떤 key를 기준으로 정리할지 람다식 넣어줌
print(users)

