# arr = [3,3,2,10,5]

# newarr = []
# for el in arr:
#     if el > 5:
#         newarr.append(el)

# print(newarr)

#필터
arr = [3,3,2,10,5]

newarr = []

# def comp(item):
#     return item > 5

newarr = list(filter(lambda el:el>5 ,arr)) #-> 리스트에 함수 적용해서 트루인것만 새 리스트 구성 (기존 배열에 담아도 관계없음)
print(newarr)
