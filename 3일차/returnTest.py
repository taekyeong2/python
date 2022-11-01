'''
리턴테스트
'''

#if 없이 중간 리턴 경우 - 잘없음
def return_test():
    print("a 위치")
    return  
    print("b위치")
    #return -> 생략가능. 따로 안적으면 맨 마지막에 있는것과 같다. 

return_test()

#조건 걸어서 중간 리턴
def return_test():
    num = int(input())
    print("a 위치")
    if (num<10):
        return
    print("b위치")

return_test()
