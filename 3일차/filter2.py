


users = [   
    {'userno':100, 'username': 'user1', 'salary':2000},
    {'userno':101, 'username': 'user2', 'salary':1000},
    {'userno':102, 'username': 'user3', 'salary':1500}
]

#급여를 가지고 필터값 알고싶다.
arr=list(filter( lambda item: item['salary']>1000  , users))  
nos = list(map( lambda i : i['userno'] , arr))
print(nos)