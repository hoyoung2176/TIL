def DFS(no, hap, start):
    global sol
    if hap >= B:
        if sol > (hap-B):
            sol = (hap-B)
        return
    if no >= N or start >= N:
        return
    for i in range(start, N):
        chk[no] = chk[i]
        DFS(no+1, hap+temp[i], i+1)



T = int(input())
for tc in range(T):
    N, B = map(int, input().split())
    temp = []
    for i in range(N):
        temp.append(int(input()))
    chk = [0] * (N+1)
    sol = 1000000000000000000000000000000000000
    DFS(0, 0, 0)
    print(sol)