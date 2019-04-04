def BFS():
    queue = []
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    zero = 0 # 0 의 개수
    r, c, day = 0, 0, 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 1:  # 익은토마토의 자리를 모두 시작점 큐에 저장
                queue.append((i, j, 0),)
            elif arr[i][j] == 0:
                zero += 1       # 0의 개수 카운트
    if zero == 0:
        return 0                # 모두 익은 상태이면 리턴

    while queue:
        r, c, day = queue.pop(0)        # 큐에서 데이터 읽기(현재 좌표)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr<0 or nr>= R or nc<0 or nc>= C:        # 맵 범위를 벗어나면 스킵
                continue
            if arr[nr][nc] == 0:
                queue.append((nr, nc, day+1))
                arr[nr][nc] = 1
                zero -= 1   # 익혀가면서 차감
    if zero:
        return -1       # 모두 못 익힌 상태이면 -1 리턴
    else:
        return day      # 모두 익힌 사태이면 최소일자 리턴


# main -------------
C, R = map(int, input().split())
arr = []
for i in range(R):
    arr.append(list(map(int, input().split())))
print(BFS())