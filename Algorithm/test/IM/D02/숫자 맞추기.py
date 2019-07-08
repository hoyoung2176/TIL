import sys
sys.stdin = open('숫자맞추기.txt')

def find(r, c):
    global arr
    if arr[r][c] == 0:
        return
    else:
        flag = 0
        for i in range(r+1, N):

            if arr[r][c] == arr[i][c]:
                arr[i][j] = 0
                flag = 1
        if flag == 1:
            arr[r][c] = 0
N = int(input())
arr = [[0 for _ in range(3)] for _ in range(N)]
ans = [0 for _ in range(N)]


for i in range(N):
    arr[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(3):
        find(i,j)
#
for i in range(N):
    print(sum(arr[i]))
# print(arr)