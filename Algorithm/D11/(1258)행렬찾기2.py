
def get_submatrix(x, y):
    global submatrix, subcnt
    i = 0
    while data[x+i][y]:
        j = 0
        while data[x+i][y+j]:
            data[x+i][y+j] = 0
            j += 1
        i += 1
    submatrix.append((i, j))  #튜플저장


import sys
sys.stdin = open("(1258)행렬찾기_input.txt","r")
T = int(input())
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    submatrix = []

    # subcnt = 0
    for i in range(N):
        for j in range(N):
            if data[i][j]:
                get_submatrix(i, j)

    submatrix.sort(key=lambda a:(a[0]*a[1], a[0]))

    print(f"#{tc+1} {len(submatrix)}", end=" ")
    for x, y in submatrix:
        print(f"{x} {y}", end=" ")
    print()
