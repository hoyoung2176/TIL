import sys
sys.stdin = open("오셀로.txt")

def check(x, y, color):
    dx = [1, -1, 0, 0, 1, 1,-1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]

    for i in range(8):
        j = 0
        nx = x + dx[i]
        ny = y + dy[i]
        while arr[nx][ny] != 9 and arr[nx][ny] != color:
            nx += dx[i]
            ny += dy[i]
            if arr[nx][ny] == 9:
                break
            elif arr[nx][ny] == color:
                return True
    return False


def result(x, y, color):
    dx = [1, -1, 0, 0, 1, 1,-1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]

    for i in range(8):
        j = 0
        nx = x + dx[i]
        ny = y + dy[i]
        while arr[nx][ny] != 9 and arr[nx][ny] != color and arr[nx][ny] != 0:
            nx += dx[i]
            ny += dy[i]
            j += 1
            if arr[nx][ny] == 9 or arr[nx][ny] == 0:
                break
            elif arr[nx][ny] == color:
                for k in range(j):
                    stack[color] += 1
                    if color == 1:
                        stack[2] -= 1
                    elif color == 2:
                        stack[1] -= 1
                    nx -= dx[i]
                    ny -= dy[i]
                    arr[nx][ny] = color



T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [[0 for _ in range(N+2)] for _ in range(N+2)]
    arr[0] = [9]*(N+2)
    arr[N+1] = [9]*(N+2)
    for i in range(1,N+1):
        arr[i][0] = 9
        arr[i][N+1] = 9
    arr[N//2][N//2] = 2
    arr[N // 2+1][N // 2] = 1
    arr[N // 2][N // 2+1 ] = 1
    arr[N // 2+1][N // 2+1] = 2
    stack = [0, 2, 2]



    for i in range(M):
        temp = list(map(int, input().split()))
        if check(temp[0], temp[1], temp[2]) == True:
            arr[temp[0]][temp[1]] = temp[2]
            stack[temp[2]] += 1
            result(temp[0], temp[1], temp[2])

    # for i in range(1, N+2):
    #     for j in range(1, N+2):
    #         if arr[i][j] == 1:
    #             stack[1] += 1
    #         elif arr[i][j] == 2:
    #             stack[2] += 1


    print("#{} {} {}".format(tc + 1, stack[1], stack[2]))