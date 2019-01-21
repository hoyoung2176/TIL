# arr = [[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# dx = [0,0,1,-1]
# dy = [-1,1,0,0]
# ans = 0
# for x in range(len(arr)):
#     for y in range(len(arr[x])):
#         for i in range(4):
#             testX = x + dx[i]
#             testY = y + dy[i]
#             if testX > 0 and testY > 0:
#                 if arr[x][y]-arr[testX][testY] > 0:
#                     ans += sum(arr[x][y] - arr[testX][testY])
#                 else:
#                     ans += sum(arr[testX][testY] - arr[x][y])
#                 print(ans)
#
"""
11111
10001
10001
10001
11111
"""


def isWall(x , y):
    if x < 0 or x >= 5:
        return True
    if y < 0 or y >= 5:
        return True


def calAbs(y , x):
    if y - x > 0:
        return y - x
    else:
        return x - y

arr = [[0 for j in range(5)] for k in range(5)] #행렬 크기고정

for i in range(5):
    arr[i] = list(map(int, input().split()))

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

sum = 0
for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            # if isWall(testX, testY) == False:
            if isWall(testX, testY) != True:
                sum += calAbs(arr[y][x], arr[testY][testX])
print("sum = {}".format(sum))