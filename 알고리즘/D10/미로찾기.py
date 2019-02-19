import sys
sys.stdin = open("미로찾기.txt")

#벽 구분
def is_wall(new_x, new_y):
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
                y = i
                x = j
                return (x, y)

def maze(x,y):
    global arr, visited, flag
    new_x = 0
    new_y = 0
    visited[y][x] = 1
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    if arr[y][x] == '3': # 가지치기 하는방법
        flag = 1
        return

    else:
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if is_wall(new_x, new_y) == True and visited[new_y][new_x] == 0:
                x = new_x
                y = new_y
                maze(x,y)

T =int(input())

for tc in range(T):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    ans = 0
    flag = 0
    for i in range(N):
        arr[i] = list(map(str, input()))
    x,y = start(N)
    maze(x,y)
    print(f"#{tc+1} {flag}")