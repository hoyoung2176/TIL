import sys
sys.stdin = open("과수원.txt")

def make_arr(r,c):
    global ans
    arr1 = [[0 for _ in range(c)] for _ in range(r)]
    arr2 = [[0 for _ in range(c)] for _ in range(r,N)]
    arr3 = [[0 for _ in range(c,N)] for _ in range(r)]
    arr4 = [[0 for _ in range(c,N)] for _ in range(r,N)]
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    #배열 1번 만들기
    for i in range(r):
        for j in range(c):
            arr1[i][j] = arr[i][j]
            if arr1[i][j] == 1:
                sum1 += 1

    #배열 2번 만들기
    for i in range(N-r):
        for j in range(c):
            arr2[i][j] = arr[r+i][j]
            if arr2[i][j] == 1:
                sum2 += 1

    # 배열 2번 만들기
    for i in range(r):
        for j in range(N - c):
            arr3[i][j] = arr[i][c+j]
            if arr3[i][j] == 1:
                sum3 += 1

    # 배열 2번 만들기
    for i in range(N - r):
        for j in range(N - c):
            arr4[i][j] = arr[r + i][c+j]
            if arr4[i][j] == 1:
                sum4 += 1


    if sum1 == sum2 == sum3 == sum4:
        ans += 1


N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input()))

ans = 0
for i in range(1, N):
    for j in range(1, N):
        make_arr(i,j)

if ans == 0:
    print(-1)
else:
    print(ans)