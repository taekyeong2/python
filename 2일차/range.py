'''
특정한 횟수만큼 반복
'''

# 1~ 10홀수
# for i in range(1,11,2): 
#     print (i)

# 0~10 짝수
# for a in range(0,11,2):
#     print(a)

# for i in range(1,11):
#     print("*"*i)

# for i in range(11,0,-2):
#     print(" "*((11-i)//2),"*"*i)


n=input()
n=int(n)
for i in range(1,n+1):
    print((n-i)*" ","*"*i)
