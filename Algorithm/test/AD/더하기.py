def DFS(no, start, hap):
    global flag
    if hap == K:
        flag = 1
        return
    if flag == 1:
        return
    if no >= N or start >= N:
        return

    for i in range(start, N):
        DFS(no+1, i+1, hap+temp[i])


T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    temp = list(map(int, input().split()))
    flag = 0
    DFS(0, 0, 0)
    if flag == 1:
        print('YES')
    else:
        print('NO')