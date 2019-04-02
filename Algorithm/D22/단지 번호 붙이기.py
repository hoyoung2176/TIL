def DFS(r, c):
    global visited, cnt
    visited[r][c] = 1

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc] != 0 or arr[nr][nc] != 1:
            continue
        elif visited[nr][nc] == 0 and arr[nr][nc] == 1:
            visited[nr][nc] = 1
            cnt += 1
            DFS(nr, nc)


N = int(input())
arr = []
arr=[list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
sol = []
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and arr[i][j] == 1:
            cnt = 1
            DFS(i, j)
            sol.append(cnt)
sol.sort()
print(len(sol))
for i in range(len(sol)):
    print(sol[i])
