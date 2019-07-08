import sys
sys.stdin = open("색종이02.txt")

N = int(input())
data = [[0 for _ in range(102)] for _ in range(102)]

for tc in range(N):
    R, C = map(int, input().split())
    for i in range(R+1, R+11):
        for j in range(C+1, C+11):
            data[i][j] = 1

cnt = 0
for i in range(102):
    for j in range(102):
        if data[i][j] == 1:
            if data[i-1][j] == 0:
                cnt += 1
            if data[i+1][j] == 0:
                cnt += 1
            if data[i][j-1] == 0:
                cnt += 1
            if data[i][j+1] == 0:
                cnt += 1

print(cnt)

