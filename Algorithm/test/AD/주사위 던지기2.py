def DFS(no, hap):
    if no>= N:
        if hap == M:
            for i in range(N):
                print(rec[i], end = ' ')
            print()
        return
    for i in range(1, 7):
        if rec[no]:
            return
        rec[no] = i
        DFS(no+1, hap+i)
        rec[no] = 0

N, M = map(int, input().split())
rec = [0]*N
DFS(0, 0)