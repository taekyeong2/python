

total = 0
score = [10,5,20,3,25]
for s in score:
    if s > 10:
        total += s
        print(s)
print("==========")
total=0  #초기화
for s in score:
    if s <= 10:
        continue  #for 문 첨으로 돌아가는것.
    total += s
    print(s)