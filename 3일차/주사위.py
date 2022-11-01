arr=input().split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if a==b==c:
    print(10000+(a*1000))
elif a==b or a==c:   
    print(1000+(a*100))
elif b==c:
    print(1000+(c*100))
else:
    # maxN = int(arr[0])
    # for i in arr:
    #     if maxN < int(i):
    #         maxN = int(i)
    # print(maxN*100)
    print(max(a,b,c)*100)