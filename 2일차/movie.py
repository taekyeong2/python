'''
영화정보
'''

boxoffice = {"boxOfficeResult":{"boxofficeType":"일별 박스오피스","showRange":"20221030~20221030","dailyBoxOfficeList":[
{"rnum":"1","rank":"1","rankInten":"0","rankOldAndNew":"OLD","movieCd":"20198429","movieNm":"자백",
"openDt":"2022-10-26","salesAmt":"687358463","salesShare":"28.4","salesInten":"-29317502","salesChange":"-4.1","salesAcc":"2488700649",
"audiCnt":"66501","audiInten":"-2754","audiChange":"-4","audiAcc":"253013","scrnCnt":"1093","showCnt":"4625"},
{"rnum":"2","rank":"2","rankInten":"0","rankOldAndNew":"OLD","movieCd":"20198461","movieNm":"리멤버","openDt":"2022-10-26","salesAmt":"492216647",
"salesShare":"20.4","salesInten":"-124205293","salesChange":"-20.1","salesAcc":"2313549512","audiCnt":"47815","audiInten":"-11475",
"audiChange":"-19.4","audiAcc":"239350","scrnCnt":"1162","showCnt":"4385"},
{"rnum":"3","rank":"3","rankInten":"0","rankOldAndNew":"OLD","movieCd":"20226886","movieNm":"블랙 아담","openDt":"2022-10-19","salesAmt":"437645543","salesShare":"18.1",
"salesInten":"-96206492","salesChange":"-18","salesAcc":"6722558455","audiCnt":"41542","audiInten":"-8335","audiChange":"-16.7","audiAcc":"649123","scrnCnt":"860","showCnt":"2788"},
{"rnum":"4","rank":"4","rankInten":"0","rankOldAndNew":"OLD","movieCd":"20226777","movieNm":"극장판 짱구는 못말려: 수수께끼! 꽃피는 천하떡잎학교",
"openDt":"2022-09-28","salesAmt":"213179058","salesShare":"8.8","salesInten":"12688289","salesChange":"6.3","salesAcc":"7000550117","audiCnt":"20850",
"audiInten":"1257","audiChange":"6.4","audiAcc":"698537","scrnCnt":"578","showCnt":"994"},
{"rnum":"5","rank":"5","rankInten":"0","rankOldAndNew":"OLD","movieCd":"20226798","movieNm":"에브리씽 에브리웨어 올 앳 원스","openDt":"2022-10-12","salesAmt":"154074206",
"salesShare":"6.4","salesInten":"-29743154","salesChange":"-16.2","salesAcc":"1913045355","audiCnt":"13374","audiInten":"-2466","audiChange":"-15.6","audiAcc":"178004","scrnCnt":"395","showCnt":"689"},
{"rnum":"6","rank":"6","rankInten":"0","rankOldAndNew":"OLD","movieCd":"20198317","movieNm":"인생은 아름다워","openDt":"2022-09-28","salesAmt":"121994111",
"salesShare":"5.0","salesInten":"-15732249","salesChange":"-11.4","salesAcc":"9992769443","audiCnt":"13124","audiInten":"-1656","audiChange":"-11.2",
"audiAcc":"1067109","scrnCnt":"573","showCnt":"1072"},
{"rnum":"7","rank":"7","rankInten":"0","rankOldAndNew":"OLD","movieCd":"20215601","movieNm":"공조2: 인터내셔날","openDt":"2022-09-07","salesAmt":"57622483",
"salesShare":"2.4","salesInten":"-9376966","salesChange":"-14","salesAcc":"70675410867","audiCnt":"8207","audiInten":"-1374","audiChange":"-14.3",
"audiAcc":"6948239","scrnCnt":"439","showCnt":"659"},
{"rnum":"8","rank":"8","rankInten":"0","rankOldAndNew":"OLD","movieCd":"20226558","movieNm":"아인보: 아마존의 전설",
"openDt":"2022-10-26","salesAmt":"54972288","salesShare":"2.3","salesInten":"6199029","salesChange":"12.7","salesAcc":"150232244","audiCnt":"6045","audiInten":"644",
"audiChange":"11.9","audiAcc":"17636","scrnCnt":"401","showCnt":"487"},
{"rnum":"9","rank":"9","rankInten":"0","rankOldAndNew":"OLD","movieCd":"20227304","movieNm":"오펀: 천사의 탄생","openDt":"2022-10-12","salesAmt":"19228883",
"salesShare":"0.8","salesInten":"-4835404","salesChange":"-20.1","salesAcc":"1750733115","audiCnt":"2068","audiInten":"-642","audiChange":"-23.7","audiAcc":"172246","scrnCnt":"163","showCnt":"209"},
{"rnum":"10","rank":"10","rankInten":"2","rankOldAndNew":"OLD","movieCd":"20227225","movieNm":"귀못","openDt":"2022-10-19","salesAmt":"15712700","salesShare":"0.6",
"salesInten":"384700","salesChange":"2.5","salesAcc":"348694600","audiCnt":"2065","audiInten":"491","audiChange":"31.2","audiAcc":"41423","scrnCnt":"110","showCnt":"143"}]}}
# print(boxoffice["boxOfficeResult"]["dailyBoxOfficeList"][0]["movieNm"])


# #영화 제목 출력
mvlist = boxoffice["boxOfficeResult"]["dailyBoxOfficeList"]
for mv in mvlist:  # 자바스트립드 of = 파이썬 in
    print(mv["rank"], mv["movieNm"])

