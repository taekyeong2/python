'''
movie
'''

import requests 
def movieRank(dt):
    url = f'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt={dt}'
    result = requests.get(url)  #서버에서 받는 모든 ㄱ값은 string
    # print(result.text)
    result = result.json()  # dictionary. list  -> 객체타입으로 변환
    dailyBoxOfficeList = result["boxOfficeResult"]['dailyBoxOfficeList']
    # print(dailyBoxOfficeList[0]['movieNm'])

    for el in dailyBoxOfficeList:  
        print(f"{el['rank']}\t{el['movieCd']}\t{el['movieNm']}")
        
# print('20221101')
# movieRank('20221101')

# print('20221001')
# movieRank('20221001')

#영화코드 입력 - 상세정보 조회 함수 선언

def movieInfo(cd):
    url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=f5eef3421c602c6cb7ea224104795888&movieCd={cd}' #내 키값을 받아서 넣어 씀
    result = requests.get(url)
    result=result.json()
    movieinfo = result["movieInfoResult"]["movieInfo"]
    print(f'영화제목\t{movieinfo["movieNm"]}')
    print(f'개봉일자\t{movieinfo["prdtYear"]}')
    print(f'상영시간\t{movieinfo["showTm"]}')

    for act in movieinfo["actors"]:   
        print(f'배우 \t {act["peopleNm"]}\t{act["cast"]}')

    print(f'감독 \t {movieinfo["directors"][0]["peopleNm"]}')

#다른곳에 모듈로 쓸때이거 실행 안하고 싶다.
if __name__ == "__main__":  # 메인모듈일떄 실행한다는 뜻
    movieInfo('20227304') 