# from random import randint
# from secrets import choice
# c = randint(1,100)
# print(c)

# cnt = 0

while True:
    from random import randint
    c = randint(1,100)
    print(c)

    cnt = 0
    while cnt < 10:
        cnt += 1
        p = input()
        p = int(p)

        if  p < c:
            print ('틀렸습니다.\n낮습니다.')
        elif p > c:
            print('틀렸습니다.\n높습니다.')
        else :
            print('축하합니다')
            break
    print("게임오버")
    exitYn = input("게임을 계속 할까요?(y/n): ")
    if exitYn in ['N','n']:
        break
