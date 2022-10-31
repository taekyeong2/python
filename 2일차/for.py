'''
반복문
'''

#list
names = ['김','이','박']

print("list====")
for obj in names:
    print(obj)

#list range
print("list range====")
for idx in range(len(names)):
    print(names[idx])

#dictionary
dict = {'no':100, 'username': 'user1', 'salary':2000}

print("dict-=====")
for key in dict:
    print(key, dict[key])

print("dict items======")
for key,value in dict.items(): #-> key, value 같이 부름.
    print(key, value)

users = [ 
    {'no':100, 'username': 'user1', 'salary':2000},
    {'no':101, 'username': 'user2', 'salary':1000},
    {'no':102, 'username': 'user3', 'salary':1500}
]
print("list dict=====")
for obj in users:
    print(obj["username"])

print('list dict range+====')
for idx in range(len(users)):
    print(users[idx]['username'])