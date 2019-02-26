import sys
sys.stdin = open('미로거리.txt')

#벽 구분
def is_wall(new_y, new_x):
    global arr
    if new_x < 0 or new_x >= N:
        return False
    if new_y < 0 or new_y >= N:
        return False
    if arr[new_y][new_x] == '1':
        return False
    return True

#스타트 지점 찾기
def start(N):
    global x, y, arr
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                return (i, j)

#도착점 찾기
def last(N):
    global x, y, arr
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '3':
                return (i, j)

#bfs 함수
def bfs(y,x):
    global arr, N, visited
    visited[y][x] = 1
    queue = []

    # x,y좌표 넣기

    queue.append((y,x),)
    while len(queue) != 0:
        y, x = queue.pop(0)
        dx = [0, 0, 1, -1]
        dy = [-1, 1, 0, 0]
        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]

            #벽과 방문여부 확인
            if is_wall(new_y, new_x) == True and  visited[new_y][new_x] == 0:

                queue.append((new_y, new_x),)
                visited[new_y][new_x]=visited[y][x]+1


T = int(input())

for tc in range(T):
    # N*N 미로
    N = int(input())

    #방문확인 2차원배열
    visited = [[0 for _ in range(N)] for _ in range(N)]

    #미로 받아오기
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(str, input()))

    #출발 좌표 찾기
    y, x = start(N)

    #도착 좌표 찾기
    last_y, last_x = last(N)

    #미로 찾기
    bfs(y,x)

    #몇 번 들렸는지 확인
    if visited[last_y][last_x] > 0:
    #2를 빼야하는 이유는 시작할때 시작점 visited 1로 시작하였고, 마지막 도착점에서도 방문 처리해주었기 때문에
        print("#{} {}".format(tc+1, visited[last_y][last_x]-2))
    # 미로에 길이 없는 경우 값이 0이 나온다.
    else:
        print("#{} {}".format(tc+1, visited[last_y][last_x]))

