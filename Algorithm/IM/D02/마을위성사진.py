import sys
sys.stdin = open('마을위성사진.txt')

N=int(input())
arr = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]
for i in range(N):
    arr.append(list(map(int, input())))


for h in range(N): #언덕인지 확인하기위해
    flag = 0
    for i in range(1,N-1):
        for j in range(1,N-1):
            if arr[i][j] > h:
                flag = 1
                if arr[i-1][j]>h and arr[i+1][j]>h and arr[i][j-1]>h and arr[i][j+1]>h:
                    arr[i][j] += 1
    if flag == 0:
        break
#
# for i in range(N):
#     for j in range(N):
#         print(arr[i][j], end=' ')
#     print()

print(h)