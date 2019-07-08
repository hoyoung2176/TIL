import sys
sys.stdin = open("원안의사각형.txt")

r = int(input())
arr = [[0 for _ in range(r+1)] for _ in range(r+1)]
cnt = 0
for i in range(1, r+1):
    for j in range(1, r+1):
        if i**2 + j**2 <= r**2:
            arr[i][j] = 1
            # cnt += 1


for i in range(1, r):
    for j in range(1, r):
        if arr[i][j]==1:
            cnt +=1
print(4*cnt)

