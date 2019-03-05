N = 5
N2= N
arr=[[0 for _ in range(N)] for _ in range(N)]
row = 0
col = -1
j = 1
inc = 1
while N > 0:
    for i in range(N):
        col += inc
        arr[row][col] += j
        j+=1


    N -= 1
    if N == 0:
        break

    for i in range(N):
        row += inc
        arr[row][col] += j
        j+=1
    inc *= -1

for i in range(N2):
    for j in range(N2):
        print(arr[i][j], end= " ")
    print()