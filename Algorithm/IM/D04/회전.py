import sys, copy
sys.stdin = open('회전.txt')

def rearr(arr):
    global Narr
    for i in range(N):
        for j in range(N):
            Narr[j][N - i - 1] = arr[i][j]
    # return Narr


N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
Narr = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))
temp = int(input())

while temp != 0:
    for i in range(temp//90):
        rearr(arr)
        arr = copy.deepcopy(Narr)
    temp = int(input())


    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ")
        print()




