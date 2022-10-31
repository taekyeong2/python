'''
합계구하기
'''

score=[10,50,100]
total = 0
for s in score:
    total += s
print('합계: ', total)


#최대최소구하기
maxScore = score[0] 
minScore = score[0]
  # 합계구할땐 0인것이 맞음.
for s in score:
    if s > maxScore :
        maxScore = s 
for s in score:
    if s < minScore :
        minScore = s 
print(maxScore, minScore)