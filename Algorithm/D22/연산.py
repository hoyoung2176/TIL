import time
start_time = time.time()


import sys
sys.stdin = open("연산.txt")

def BFS(n):
    global visited
    queue = []
    # queue+=[n]
    queue.append(n)
    visited[n] = 1
    x = 0
    while queue:
        n = queue[x]
        dx = [n +1 , n-1, n * 2, n - 10]
        for i in range(4):
            nn=dx[i]
            # if i == 0:
            #     nn = n + 1
            # elif i == 1:
            #     nn = n - 1
            # elif i == 2:
            #     nn = n * 2
            # elif i == 3:
            #     nn = n - 10

            if nn == M:
                visited[nn] = visited[n] + 1
                return visited[nn]
            if nn > 0 and nn <= 1000000 and visited[nn] == 0:
                visited[nn] = visited[n] + 1
                # queue += [nn]
                queue.append(nn)
        x += 1

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    visited = [0] * (1000001)
    BFS(N)
    print('#{} {}'.format(tc, visited[M]-1))
print(time.time() - start_time, 'seconds')
