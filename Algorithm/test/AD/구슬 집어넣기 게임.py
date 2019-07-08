def start():
    flag = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'R':
                Rr, Rc = i, j
                arr[i][j] = '.'
                flag += 1
            elif arr[i][j] == 'B':
                Br, Bc = i, j
                arr[i][j] = '.'
                flag += 1
            elif arr[i][j] == 'H':
                Hr, Hc = i, j
                arr[i][j] = '.'
                flag += 1
            if flag == 3:
                break
        if flag == 3:
            break
    return Rr, Rc, Br, Bc, Hr, Hc




def BFS(Rr, Rc, Br, Bc, Hr, Hc):
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]
    que = []
    que.append((Rr, Rc, Br, Bc, 0))     #Rr, Rc, Br, Bc, cnt
    while que:
        Rr, Rc, Br, Bc, cnt = que.pop(0)
        # 기울임 횟수가 10회가 넘어서면 게임 실패이다.
        if cnt >= 10:
            break
        for i in range(4):
            nRr, nRc = Rr + dr[i], Rc + dc[i]
            nBr, nBc = Br + dr[i], Bc + dc[i]
            # 이동 방향에 벽이 있는 구슬은 움직일 수 없다.
            if arr[nRr][nRc] == '#':    # 빨간 구슬의 가볼위치가 벽이면 현재위치로
                nRr, nRc = Rr, Rc

            if arr[nBr][nBc] == '#':    # 빨간 구슬의 가볼위치가 벽이면 현재위치로
                nBr, nBc = Br, Bc

            # 빨간 구슬과 파란 구슬이 같은 위치이면 스킵
            if nRr == nBr and nRc == nBc:
                continue

            # 파란 구슬이 목표 구멍이면 스킵
            if nBr == Hr and nBc == Hc:
                continue

            # 빨간 구슬이 목표구멍이면 성공 리턴
            if nRr == Hr and nRc == Hc:
                return cnt+1

            # 가볼 위치의 빨간구슬위치와 파란구슬위치를 방문했으면 스킵
            if chk[nRr][nRc][nBr][nBc]:
                continue
            # 여기까지 오면 큐에 저장하고 방문표시
            chk[nRr][nRc][nBr][nBc] = 1
            que.append((nRr, nRc, nBr, nBc, cnt + 1))



    return -1



T = int(input())


for tc in range(T):
    R, C = map(int, input().split())
    arr = [list(input()) for _ in range(R)]
    chk = [[[[0]*C for _ in range(R)] for _ in range(C)] for _ in range(R)]             # chk[Rr][Rc][Br][Bc]
    Rr, Rc, Br, Bc, Hr, Hc = start()
    print(BFS(Rr, Rc, Br, Bc, Hr, Hc))