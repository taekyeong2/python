
arr = list(map(int, input().split(" "))) #-> arr의 요소를 하나씩 다 읽어서 인트형으로 변환

# for i in range(len(arr)):
#     arr[i] = int(arr[i])

# for i in range(len(arr)):s
#      arr[i] = arr[i]*arr[i]


# arr = [1,2,3,4,5]

# for i in range(len(arr)):
#     arr[i] = arr[i] ** 2


# def power(item):
#     return item**2


# arr = map(power,arr)  #->각각의 배열에 함수 적용해서 새로운 리스트 


arr = list(map(lambda item : item**2 ,arr))  #-> lambda 매개값 : 리턴값

for el in arr:
    print(el)