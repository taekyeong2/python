'''
#open
file = open('d:/basic.txt','r')
#read
txt = file.read()
print(txt)
#close
file.close()
'''

#open
with open('d:/basic.txt','r') as file:
    #한 줄씩 처리
    lines = file.readlines()  #파일 내용을 각각 라인으로 자른것.
    for line in lines:
        info = line.split(" ")
        print(info[1])
