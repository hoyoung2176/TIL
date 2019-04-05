def DFS(no, start, T):
    global sol
    if sol < T:
        return
    if no >= N+1 or start >= N+1:
        # for i in range(N):
        #     print(chk[i], end=' ')
        # print()
        if sol > T:
            sol = T
        return
    cnt = 0
    for i in range(start, N+1):
        cnt += temp[i]
        if M < cnt:
            return
        elif M >= cnt:
            # chk[i] = 1
            DFS(no + 1, i + 1, T + t[i])
            # chk[i] = 0


M = int(input())
N = int(input())
temp = list(map(int, input().split()))
t = list(map(int, input().split())) + [0]
sol = 1000000000
# chk = [0] * N
DFS(0, 0, 0)
print(sol)