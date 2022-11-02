'''
제일 큰 수 찾는 함수
매개변수 : 정수형값들
리턴값 : 정수형

'''

# from cgitb import reset
# from unittest import result


def max(*nums):
    #결과(제일큰수)를 지정할 변수에 첫번째 요소로 초기화
    max = nums[0]
    # 리스트 수만큼 반복
    for num in nums:
        #리스트 수만큼 반복하면서 큰 수인지 검사
        if max < num:
            #리스트 값이 크다면 변수에 저장
            max = num
    #결과를 리턴
    return max


'''result=max(3,5,10,2)
print(result)

result=max(100,50)
print(result)'''