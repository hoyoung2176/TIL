import sys
sys.stdin = open("사냥꾼.txt")

def find(r, c):
    global cnt, kill
    dr = [1, -1, 0, 0, 1, 1, -1, -1]
    dc = [0, 0, 1, -1, 1, -1, 1, -1]
    x , y = r, c
    i = 0
    while i < 8:
        r = r + dr[i]
        c = c + dc[i]
        if arr[r][c] == '2' and kill[r][c] == 0:
            kill[r][c] = 1
            cnt += 1
        if arr[r][c] == '1' or arr[r][c] == '0':
            i += 1
            r, c = x, y





N = int(input())
arr = [['0' for _ in range(N+2)] for _ in range(N+2)]
cnt = 0
for i in range(1, N+1):
    arr[i] = ['0'] + list((input())) + ['0']

kill = [[0 for _ in range(N+2)] for _ in range(N+2)]

for i in range(1,N):
    for j in range(1,N):
        if arr[i][j] == '1':
            find(i,j)
print(cnt)
