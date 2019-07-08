import sys
sys.stdin = open("미로탈출 로봇중간 단계.txt")

N = int(input())
arr = [['1' for _ in range(N+2)] for _ in range(N+2)]

for i in range(1, N+1):
    temp = list(input())
    for j in range(1,N+1):
        arr[i][j] = temp[j-1]


data = list(map(int, input().split()))
i = 0
x, y = 1, 1
cnt = 0
while True:
    if data[i] == 1:
        arr[x][y] = '2'
        x += 1
        cnt += 1
        if arr[x][y] == '1':
            cnt -= 1
            x -= 1
            if i >= (len(data)-1):
                i = 0
            else:
                i += 1
        elif arr[x][y] == '2':
            cnt -= 1
            break
    elif data[i] == 2:
        arr[x][y] = '2'
        y -= 1
        cnt += 1
        if arr[x][y] == '1':
            cnt -= 1
            y += 1
            if i >=(len(data)-1):
                i = 0
            else:
                i += 1
        elif arr[x][y] == '2':
            cnt -= 1
            break
    elif data[i] == 3:
        arr[x][y] = '2'
        x -= 1
        cnt += 1
        if arr[x][y] == '1':
            cnt -= 1
            x += 1
            if i >=(len(data)-1):
                i = 0
            else:
                i += 1
        elif arr[x][y] == '2':
            cnt -= 1
            break
    elif data[i] == 4:
        arr[x][y] = '2'
        y += 1
        cnt += 1
        if arr[x][y] == '1':
            cnt -= 1
            y -= 1
            if i >=(len(data)-1):
                i = 0
            else:
                i += 1
        elif arr[x][y] == '2':
            cnt -= 1
            break


print(cnt)