def solve(x,y,sum):
    global ans

    if ans <= sum:
        return

    dx = [0, 1]
    dy = [1, 0]

    if x == N-1 and y == N-1:
        if ans > sum:
            ans = sum
    else:
        for i in range(2):
            nx = x +dx[i]
            ny = y + dy[i]
            if nx < N and ny <N:
                solve(nx, ny, sum + arr[nx][ny])

