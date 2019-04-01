


def perm(n,k, cursum):
    if ans < cursum:
        return
    if n == k:
        calc(n,k,cursum)
    else:
        for i in range(k,n):
            arr[i+1], arr[k+1] = arr[k+1], arr[i+1]
            perm(n, k+1, cursum +dist[arr[k]][arr[k-1]])
            arr[i + 1], arr[k + 1] = arr[k + 1], arr[i + 1]


for tc in range(T):
    ans = 100000000000
    N = int(input())
    arr = [0]*N + [0]
    for i in range(N):
        arr[i] = i
    dist = [list(map(int, input().split())) for _ in range(N)]
    perm(N-1,0,0)
    print("#{} {}".format(tc+1, cursum))
