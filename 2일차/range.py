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


n=int(input())
for i in range(1,n+1):
    #공백출력
    for j in range(n-i):
        print(" ",end="") # end="(\n)" / 기본값으로 들어있는 \n값을 빼주는것임.
    #별출력
    for j in (range(i)):
        print("*",end="")
    print()

output=""\
for i in range(1,n+1):
    #공백출력
    for j in range(n-i):
        output+=" "
    #별출력
    for j in (range(i)):
       output+="*"
    output+='\n'
print(output)
