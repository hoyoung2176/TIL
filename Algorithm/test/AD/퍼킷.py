def DFS(no, S, B, T, start):
    global sol, rec
    if no > 0:
        if sol > T:
            sol = T

    if no >= N or start >= N:

        return

    for i in range(start, N):
        nS = S * temp[i][0]
        nB = B + temp[i][1]
        nT = abs(nS - nB)
        DFS(no+1, nS, nB, nT, i+1)


N = int(input())
temp = [list(map(int, input().split())) for _ in range(N)]
sol = 100000000000000
rec = []
chk = [0] * N
DFS(0, 1, 0, 0, 0)

print(sol)