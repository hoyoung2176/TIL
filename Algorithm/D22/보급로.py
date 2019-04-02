import time
start_time = time.time()

import sys
sys.stdin = open("보급로.txt")

def BFS(r, c):
    global visited
    queue = [(0, 0),]
    x = 0
    while queue:
        if len(queue) <= x:
            break
        else:
            r, c = queue[x]
            # r, c = queue.pop(0)
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if nr == N-1 and nc == N-1:
                    hight = temp[nr][nc]
                    if visited[nr][nc] > visited[r][c] + hight:
                        visited[nr][nc] = visited[r][c] + hight

                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue
                else:
                    hight = temp[nr][nc]
                    if visited[nr][nc] > visited[r][c] + hight:
                        visited[nr][nc] = visited[r][c] + hight
                        queue.append((nr, nc),)
            x += 1
    return visited

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    temp = []
    for i in range(N):
        temp.append(list(map(int, input())))
    visited = [[9999999999 for _ in range(N)] for _ in range(N)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    visited[0][0] = 0
    BFS(0, 0)
    print('#{} {}'.format(tc, visited[N-1][N-1]))
print(time.time() - start_time, 'seconds')