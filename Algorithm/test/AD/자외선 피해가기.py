def BFS(r, c):
    global sol,visited
    queue = []
    queue.append((r, c),)
    visited[0][0] = arr[0][0]
    while queue:
        r, c = queue.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            # if 0 <= nr <= N-1 and 0 <= nc <= N-1:
            if visited[nr][nc] > visited[r][c] + arr[nr][nc]:
                visited[nr][nc] = visited[r][c] + arr[nr][nc]
                queue.append((nr, nc),)
    return visited[N-1][N-1]


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[100000] * (N) for _ in range(N)]

dr = [1, 0, 0, -1]
dc = [0, 1, -1, 0]
sol = 1000000000

print(BFS(0, 0))