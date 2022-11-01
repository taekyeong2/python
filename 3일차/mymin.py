'''
최소값 구하기
'''

def mymin(*nums):
    min=nums[0]
    for num in nums:
        if min > num:
            min = num
    return min 

print(mymin(2,3,5,234,5))
print(mymin(5,3,44,5,7,5))

        