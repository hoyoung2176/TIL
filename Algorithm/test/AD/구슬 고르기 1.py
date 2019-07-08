

def DFS(no):
    if no >= N+1:
        print(*chk)
        return
    chk[no-1] = no
    DFS(no+1)
    chk[no-1] = 0
    DFS(no + 1)

N = 3
chk = [0] * N
DFS(1)