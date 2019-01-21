num = 785868
c =[0]*12 #각자리 숫자의 수를 추출하여 갯수로 변환 #i+2가 있기때문에 12개만들어야함

for i in range(6):
    c[num % 10] += 1 #10으로 나누고 나머지 ->맨뒷글자 추출됨->처음에 3이 나옴
    num //=10   #num = num//10
                # 몫이 10이면 다시 위로 올라가서 계산
                #정수를 잘라서 리스트안으로 들어가짐
print(c)
i =0
tri = run = 0
while i < 10 :
    if c[i] >= 3 : #triplete 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1: #run 조사 후 데이터 삭제
        c[i] -= 1
        c[i+1] -=1
        c[i+2] -=1
        run +=1
        continue
    i += 1
if run + tri == 2: print("Baby Gin")
else : print("Lose")