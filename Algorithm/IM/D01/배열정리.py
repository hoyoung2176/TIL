import sys
sys.stdin = open("배열정리.txt")

N, M = map(int, input().split())
data = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    data[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(M):
        if data[i][j] == 1:
            if j-1 >= 0:
                data[i][j] += data[i][j-1]
        print(data[i][j], end=' ')
    print()

