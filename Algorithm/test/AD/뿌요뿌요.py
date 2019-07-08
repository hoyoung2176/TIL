import sys
sys.stdin = open("뿌요뿌요.txt")

def Gravity(c):
    stack = []
    for i in range(R - 1, -1, -1):
        if arr[i][c] != '.':
            stack.append(arr[i][c])
            arr[i][c] = '.'

    j = R-1
    while stack:
        arr[j][c] = stack.pop(0)
        j -= 1

def BFS(r, c):      #그룹안에 같은색이 4개 인것 찾기
    global sol, chk
    if chk[r][c]:
        return
    color = arr[r][c]
    queue = [(r, c)]
    stack = [(r, c)]

    chk[r][c] = 1
    cnt = 0
    while queue:
        r, c = queue.pop(0)
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue
            if chk[nr][nc]:
                continue
            if arr[nr][nc] == color:
                cnt += 1
                chk[nr][nc] = 1
                stack.append((nr, nc))
                queue.append((nr, nc))


    # 그룹안에 같은색이 4개이면 터트리기

    if cnt >= 3:
        data.append((stack),)


def PuyoPuyo(stack):
    global sol
    if stack:
        chkc = [0] * C
        while stack:
            temp = stack.pop(-1)
            while temp:
                r, c = temp.pop(-1)
                arr[r][c] = '.'
                if not chkc[c]:
                    chkc[c] = 1


        # 터트린 자리 복구하기
        for i in range(C):
            if chkc[i]:
                Gravity(i)

        return 0
    else:
        return 1


T = int(input())
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
R, C = 12, 6
for tc in range(T):
    sol = 0
    arr = [list(input()) for _ in range(R)]
    data = []
    flag = 0
    while flag == 0:
        chk = [[0] * C for _ in range(R)]
        for i in range(R-1, -1, -1):
            for j in range(C):  # 색깔 찾기
                if arr[i][j] != '.':
                    BFS(i,j)
        sol += 1
        flag = PuyoPuyo(data)
    print(sol-1)