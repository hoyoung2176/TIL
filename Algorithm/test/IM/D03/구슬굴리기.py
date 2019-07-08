import sys
sys.stdin = open("구슬 굴리기.txt")

def find(r,c):
    global cnt
    x, y = r, c
    # 1번 윗 방향 2번 아랫방향, 3번 왼쪽, 4번 오른쪽
    dr = [0, -1, 1, 0, 0]
    dc = [0, 0, 0, -1, 1]
    i=0
    while i < len(data):
        r = r + dr[data[i]]
        c = c + dc[data[i]]
        if arr[r][c] == '0':
            arr[r][c] = '9'
            cnt += 1
        elif arr[r][c] == '1':
            r = r - dr[data[i]]
            c = c - dc[data[i]]
            i += 1








R, C = map(int, input().split())
arr = [['1' for _ in range(C+2)] for _ in range(R+2)]
for i in range(1, R+1):
    arr[i] = ['1'] + list((input())) + ['1']
N = int(input())
data = list(map(int, input().split()))
cnt = 1
for i in range(1, R + 2):
    for j in range(1, C + 2):
        if arr[i][j] == '2':
            find(i, j)

print(cnt)
# for i in range(R+2):
#     for j in range(C+2):
#         print(arr[i][j], end=" ")
#     print()