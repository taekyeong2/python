'''
계산기 만들기 테스트
'''

'''from calc import add, miu, mul, div

a=5
b=3    

add(a,b)  #(a,b)-> 매번 매개변수 입력하는것도 귀찮
miu(a,b)
mul(a,b)
div(a,b)'''

#클래스사용
from calClass import CalClass


# cc.a=10   #-> self때문에 매번 a,b를 넣을 필요 없음
# cc.b=20  
cc = CalClass(10,2)  # => 객체생성
cc.add()  
cc.miu()

cc = CalClass(100,20)
cc.mul()
cc.div()
