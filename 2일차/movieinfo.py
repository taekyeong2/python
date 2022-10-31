info = {
"movieInfoResult": {
"movieInfo": {
"movieCd": "20198429",
"movieNm": "자백",
"movieNmEn": "Confession",
"movieNmOg": "",
"showTm": "105",
"prdtYear": "2020",
"openDt": "20221026",
"prdtStatNm": "개봉",
"typeNm": "장편",
"nations": [
{
"nationNm": "한국"
}
],
"genres": [
{
"genreNm": "범죄"
},
{
"genreNm": "스릴러"
}
],
"directors": [
{
"peopleNm": "윤종석",
"peopleNmEn": "YOON Jong-seok"
}
],
"actors": [
{
"peopleNm": "소지섭",
"peopleNmEn": "SO Ji-sub",
"cast": "",
"castEn": ""
},
{
"peopleNm": "김윤진",
"peopleNmEn": "KIM Yun-jin",
"cast": "",
"castEn": ""
},
{
"peopleNm": "나나",
"peopleNmEn": "Nana",
"cast": "",
"castEn": ""
},
{
"peopleNm": "최광일",
"peopleNmEn": "CHOI Gwang-il",
"cast": "",
"castEn": ""
}
],
"showTypes": [
{
"showTypeGroupNm": "2D",
"showTypeNm": "디지털"
}
],
"companys": [
{
"companyCd": "20100540",
"companyNm": "리얼라이즈픽쳐스(주)",
"companyNmEn": "Realies Pictures, Inc.",
"companyPartNm": "제작사"
},
{
"companyCd": "20188021",
"companyNm": "롯데컬처웍스(주)롯데엔터테인먼트",
"companyNmEn": "Lotte Entertainment",
"companyPartNm": "배급사"
},
{
"companyCd": "20188021",
"companyNm": "롯데컬처웍스(주)롯데엔터테인먼트",
"companyNmEn": "Lotte Entertainment",
"companyPartNm": "제공"
}
],
"audits": [
{
"auditNo": "2020-MF02517",
"watchGradeNm": "15세이상관람가"
}
],
"staffs": []
},
"source": "영화진흥위원회"
}
}

#출연배우
actors = info["movieInfoResult"]["movieInfo"]["actors"] # -> 배열이 있는 것까지 가지고 와야함/
for act in actors :
    print(act["peopleNm"])

#감독
director = info["movieInfoResult"]["movieInfo"]["directors"] # -> 배열이 있는 것까지 가지고 와야함/
for dir in director :
    print("※",dir["peopleNm"])