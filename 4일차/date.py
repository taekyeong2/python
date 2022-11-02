'''
datetest
'''


from datetime import datetime

now = datetime.now()  #현재날짜 시간 불러옴.

#오늘날짜 출력 
print(now.year)
print(now.month)    
#현재시간 출력
print(now.hour)
print(now.minute)

'''
자바스크립트에서는

const d = new Date();
d.getFullYear();
https://www.w3schools.com/js/js_date_methods.asp
https://www.w3schools.com/jsref/met_win_setinterval.asp -> 함수 계쏙 실행
'''