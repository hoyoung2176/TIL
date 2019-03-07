

c ,r = map(int, input().split())
K = int(input())

arr = [[0 for _ in range(c+2)] for _ in range(r+2)]
for i in range(1,r+1):
    for j in range(1, c+1):
        arr[i][j] = 1

n = 1
x, y = r+1, 1
cnt = 0
flag = 0
while n < r*c:
    #위로 이동
    for i in range(r-cnt):
        x -= 1
        arr[x][y] = n
        n += 1
    cnt += 1

    #오른쪽으로 이동
    for i in range(c-cnt):
        y += 1
        arr[x][y] = n
        n += 1

    #아래쪽으로 이동
    for i in range(r-cnt):

        x += 1
        arr[x][y] = n
        n += 1
    cnt += 1

    #위쪽으로 이동
    for i in range(c-cnt):
        y -= 1
        arr[x][y] = n
        n += 1

# print(x, y)

cnt = 0
for i in range(r+2):
    for j in range(c+2):
        if arr[i][j] == K:
            cnt = 1
            print(j, r-i+1)
if cnt == 0:
    print(0)
    #     print(arr[i][j], end=" ")
    # print()

