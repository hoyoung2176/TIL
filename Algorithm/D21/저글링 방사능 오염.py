def bfs(r, c):
    global arr, queue, visited
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    arr[r][c] = 0
    queue.append((r,c),)
    while len(queue) != 0:
        r, c = queue.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= Y or nc < 0 or nc >= X:
                continue

            elif visited[nr][nc] == 0 and arr[nr][nc] == 1:
                visited[nr][nc] = visited[r][c] + 1
                arr[nr][nc] = 0
                queue.append((nr, nc),)


X, Y = map(int, input().split())

arr = []
queue = []
for i in range(Y):
    arr.append(list(map(int, input())))

visited = [[0 for i in range(X)] for j in range(Y)]
x1, y1 = map(int, input().split())
bfs(y1-1, x1-1)
cnt = 0
times = 0
for i in range(Y):
    for j in range(X):
        if times < visited[i][j]:
            times = visited[i][j]
        if arr[i][j] == 1:
            cnt += 1
print(times+3)
print(cnt)
