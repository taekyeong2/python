'''
딕셔너리(객체) 사용법
'''

# info={"name":"홍길동","age":20}
# print(info['name']) # -> 키 값을 넣어 찾을때 대괄호 써야함.

info={}

#이름
info["name"]=input("이름입력: ")
#나이
info["age"]=input("나이입력: ")
#주소
info["addr"]=input("주소입력: ")

print(info)

for k in info: # k -> 키(name, age, addr)값 / 키 갯수만큼 반복
    # print(f"{k}\t{info[k]}")
    print(f"{k}\t{info[k]}")


#주소 지우기
# del info["addr"]
# print(info)