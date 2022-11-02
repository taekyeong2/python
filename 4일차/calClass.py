'''
클래스 - 데이터와 함수를 같이 가지고 있는것
'''
#클래스 = 데이터 + 함수
class CalClass:
    #멤버변수
    a =0
    b =0   # 함수 부를때마다 매개변수 부를필요없당

    #생성자(함수): 객체생성시에 변수 초기화
    def __init__(self, a,b):  # class생성할때 넣어주는 값 (이름고정)
                              #- 자기자신 데이터를 초기화 ( cc=10 / 이런식으로 안해도 초기화 시켜줌)
        self.a = a
        self.b = b

    #멤버함수  = 메소드
    def add(self):    # self ->자기자신
        print(self.a + self.b)  # self.a -> 자기자신의 a

    def miu(self):
        print(self.a-self.b)

    def mul(self):
        print(self.a*self.b)

    def div(self):
        print(self.a/self.b)
