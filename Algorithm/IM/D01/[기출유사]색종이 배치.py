import sys
sys.stdin = open("색종이 배치.txt")

#첫번째 색종이에 테두리를 둘러서 판별한다.

result = 0
arr = [[0 for _ in range(102)] for _ in range(102)]

R_1, C_1, x_1, y_1 = map(int, input().split())

for i in range(R_1, R_1+x_1+2):
    for j in range(C_1, C_1+y_1+2):
        if i == R_1 or j == C_1 or i == R_1+x_1+1 or j == C_1+y_1+1:
            arr[i][j] = 2
        else:
            arr[i][j] = 1

R_2, C_2, x_2, y_2 = map(int, input().split())
cnt = 0
for j in range(R_2+1, R_2+x_2+1):
    for k in range(C_2+1, C_2+y_2+1):
        if arr[j][k] == 1:
            result = 3
        elif arr[j][k] == 2:
            cnt += 1


if result == 3:
    print(3)

else:
    if cnt == 0:
        print(4)
    elif cnt == 1:
        print(1)
    elif cnt > 1:
        print(2)




