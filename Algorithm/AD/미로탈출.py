def start(que):
    flag = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 3:
                flag = 1
                chk[0][i][j] = 1
                que.append((i, j, 0, 3))      # r, c, 이동거리, boom
                break
        if flag:
            break
    return que

def end():
    flag = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 4:
                flag = 1
                break
        if flag:
            break
    return i, j


def BFS():
    que = []
    start(que)
    er, ec = end()
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    flag = 0

    while que:
        r, c, cnt, boom = que.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr == er and nc == ec:
                flag = 1
                return cnt+1
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue
            if chk[boom][nr][nc]:
                continue
            if arr[nr][nc] == 1:
                continue
            elif arr[nr][nc] == 0:
                chk[boom][nr][nc] = 1
                que.append((nr, nc, cnt+1, boom))
            elif arr[nr][nc] == 2 and boom > 0 and chk[boom-1][nr][nc] == 0:
                chk[boom-1][nr][nc] = 1
                que.append((nr, nc, cnt+1, boom-1))

    if flag:
        return cnt
    else:
        return -1


R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
chk = [[[0] * C for _ in range(R)] for _ in range(4)]       #chk[폭탄갯수][r][c]
print(BFS())