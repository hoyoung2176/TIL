def maze(r, c):
    global arr, queue
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    arr[r][c] = 1
    queue.append((r,c),)
    while len(queue) != 0:
        r, c = queue.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nc == x2-1 and nr == y2-1:
                arr[nr][nc] = arr[r][c] + 1
                return arr[nr][nc] - 1
            if nr < 0 or nr >= Y or nc < 0 or nc >= X:
                continue

            elif arr[nr][nc] == 0:
                arr[nr][nc] = arr[r][c] + 1
                queue.append((nr, nc),)






X, Y = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
arr = []
queue = []
for i in range(Y):
    arr.append(list(map(int, input())))
print(maze(y1-1, x1-1))
