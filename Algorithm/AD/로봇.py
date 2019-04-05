def BFS():
    # 정보 테이블, 인덱스 0: 동, 1: 서, 2:남, 3:북
    dr = (0, 0, 0, 1, -1)
    dc = (0, 1, -1, 0, 0)
    turn = [(0, 0), (4, 3), (3, 4), (1, 2), (2, 1)]

    # 1] 시작점을 큐에 저장(방문표시)
    queue = [(sr, sc, sdir, 0),] # 행, 열, 방향, 명령횟수
    chk[sdir][sr][sc] = 1

    while queue:
        # 2] 큐에서 데이터 읽기
        r, c, dir, cnt = queue.pop(0)
        if r == er and c == ec and dir == edir:
            return cnt

        for i in range(1, 4):   # go 1, 2, 3, i는 증감치
            nr = r + dr[dir] * i
            nc = c + dc[dir] * i
            if nr < 0 or nr >= R or nc < 0 or nc >= C:    #벽너머로 가는지 확인
                break
            if arr[nr][nc] == 1:    # 벽이면 break
                break
            if chk[dir][nr][nc]: #길이지만 방문 했으면 스킵
                continue
            queue.append((nr, nc, dir, cnt+1),)
            chk[dir][nr][nc] = 1

        for i in range(2):      # Turn lift, right
            ndir = turn[dir][i]
            if chk[ndir][r][c]:
                continue
            queue.append((r, c, ndir, cnt + 1), )
            chk[ndir][r][c] = 1





# main--------------------------------------
R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
chk = [[[0]*C for _ in range(R)] for _ in range(5)]     # 3차원 배열// [면][행][열]
sr, sc, sdir = map(int, input().split())
er, ec, edir = map(int, input().split())
sr -= 1
sc -= 1
er -= 1
ec -= 1
print(BFS())