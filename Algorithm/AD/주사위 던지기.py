def DFS(no):
    global sol
    if sol > M:
        return

    if no >= N:
        if sol == M:
            for i in range(N):
                if cnt[i] == 1:
                    print(cnt)
                    print(i+1, end=" ")
            print()
        return

    for i in range(N):
        sol += i
        DFS(no+1)
        sol -= i

N, M = map(int, input().split())
cnt = [0] * N
sol = 0

DFS(0)