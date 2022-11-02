class StdScore:
    #함수만 배포하는 모듈과 달리 데이터까지 묶어서 배포가능
    
    std = [  ]
          
    def matTotal(self):
        matSum = 0
        for score in self.std:
            matSum += score['mat']
        print(matSum)
                                    

stdScore=StdScore()  #클래스 호출
stdScore.std = [
        {'mat':50, 'eng':90},
        {'mat':70, 'eng':80},
        {'mat':80, 'eng':60} 
] #변수 호출
stdScore.matTotal() # 함수 호출

