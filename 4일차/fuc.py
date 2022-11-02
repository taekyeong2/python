
def matTotal(std):
    matSum = 0
    for score in std:
        matSum += score['mat']
    print(matSum)
                                     #함수를 만들어놓으면 matTotal을 다른 모듈에서 쓸 수 있다.


std = [
    {'mat':50, 'eng':90},
    {'mat':70, 'eng':80},
    {'mat':80, 'eng':60}
]

matTotal(std)