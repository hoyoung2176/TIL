import sys
sys.stdin = open("같은모양찾기(3차원).txt")

M = int(input())
Marr=[]
for i in range(M):
    Marr.append(list(map(int, input())))

P=int(input())
Parr=[]
for i in range(P):
    Parr.append(list(map(int, input())))

sol = 0
#원본패턴
for i in range(M-P+1):
    for j in range(M-P+1):
        cnt= 0
        for k in range(P):
            for l in range(P):
                if Marr[i+k][j+l] == Parr[k][l]:
                    cnt+=1
        if cnt == P*P:
            sol += 1

#90도 회전한 패턴
Parr90 = [[0]*P for _ in range(P)]
for i in range(P):
    for j in range(P):
        Parr90[j][P-i-1] = Parr[i][j]

for i in range(M-P+1):
    for j in range(M-P+1):
        cnt= 0
        for k in range(P):
            for l in range(P):
                if Marr[i+k][j+l] == Parr90[k][l]:
                    cnt+=1
        if cnt == P*P:
            sol += 1

# 180도 회전한 패턴
Parr180 = [[0] * P for _ in range(P)]
for i in range(P):
    for j in range(P):
        Parr180[j][P - i - 1] = Parr90[i][j]

for i in range(M - P + 1):
    for j in range(M - P + 1):
        cnt = 0
        for k in range(P):
            for l in range(P):
                if Marr[i + k][j + l] == Parr180[k][l]:
                    cnt += 1
        if cnt == P * P:
            sol += 1

# 270도 회전한 패턴
Parr270 = [[0] * P for _ in range(P)]
for i in range(P):
    for j in range(P):
        Parr270[j][P - i - 1] = Parr180[i][j]

for i in range(M - P + 1):
    for j in range(M - P + 1):
        cnt = 0
        for k in range(P):
            for l in range(P):
                if Marr[i + k][j + l] == Parr270[k][l]:
                    cnt += 1
        if cnt == P * P:
            sol += 1

print(sol)
