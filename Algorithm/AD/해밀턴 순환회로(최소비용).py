def DFS(city, cnt, hap):
    global sol, flag
    if sol < hap:       # 가지치기
        return
    if cnt == N:        # 마지막 도시에서 집으로 가는 최소비용 비교
        if arr[city][0]:    # (단 집으로 가는 비용이 있는 경우)
            if hap + arr[city][0] < sol:
                flag = 1
                sol = hap + arr[city][0]
        return

    # 현재 도시에서 비용이 있고 방문 안한 도시를 모두 시도
    for i in range(1, N):   #가볼도시(열)
        if arr[city][i] and not visited[i]:
            visited[i] = 1
            DFS(i, cnt + 1, hap+arr[city][i])
            visited[i] = 0





N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0]*(N+1)
flag = 0
cnt = 0
sol = 10000000000
rec = []
DFS(0, 1, 0)

if flag:
    print(sol)
else:
    print(0)