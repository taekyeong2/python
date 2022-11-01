'''
가변매개변수 (*)
tuple : list와 동일한데 요소값을 변경불가함
list :[]
tuple :()
'''

'''
주석 다는법 ==>
설명 : 합계계산
매개변수 : 정수형 여러개 
리턴값 : 정수형 합계
'''
def mysum(*nums):  
    # print(type (nums))
    total = 0
    for num in nums:
        total += num
    # print(total)
    return total


t = mysum(10,20)
print(t)
print(mysum(10,20,30))
print(mysum(10,20,3,3,5,6,4,6))