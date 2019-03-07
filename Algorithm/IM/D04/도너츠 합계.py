import sys
sys.stdin = open("도너츠 합계.txt")

def find(r, c):
    ans = 0
    Dno = 0
    #오른쪽 이동
    for i in range(K-Dno):
        c += 1
        ans += arr[r][c]
    Dno += 1

    #아래이동
    for i in range(K-Dno):
        r += 1
        ans += arr[r][c]

    #왼쪽이동
    for i in range(K-Dno):
        c -= 1
        ans += arr[r][c]
    Dno += 1

    #위로 이동
    for i in range(K-Dno):
        r -= 1
        ans += arr[r][c]
    return ans
N, K = map(int,input().split())
arr = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))

max_sum = 0
for i in range(N-K+1):
    for j in range(N-K+1):
        result = find(i, j - 1)
        if max_sum < result:
            max_sum = result



print(max_sum)



