import time
start_time = time.time()

import sys
sys.stdin = open("최소비용.txt")

def BFS(r, c):
    global visited
    queue = [(0, 0),]
    while queue:
        r, c = queue.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            else:
                hight = 0
                if temp[nr][nc]-temp[r][c] > 0:
                    hight = temp[nr][nc]-temp[r][c]
                if visited[nr][nc]> visited[r][c] +hight+1:
                    visited[nr][nc] = visited[r][c] + hight +1
                    queue.append((nr, nc), )

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    temp = []
    for i in range(N):
        temp.append(list(map(int, input().split())))
    visited = [[9999999999 for _ in range(N)] for _ in range(N)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    visited[0][0] = 0
    BFS(0, 0)
    print('#{} {}'.format(tc, visited[N-1][N-1]))
print(time.time() - start_time, 'seconds')