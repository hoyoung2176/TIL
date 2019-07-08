import sys
sys.stdin = open('같은모양찾기.txt')
#
# def check(i,j):
#     global pArr, arr, cnt, M
#     if pArr[0][0] == arr[i][j]:
#         flag = 0
#         for x in range(M): #패턴행
#             if flag == 1:
#                 break
#             else:
#                 for y in range(M): #패턴열
#                     if pArr[x][y] != arr[i+x][j+y]:
#                         flag = 1
#                         break
#                     else:
#                         cnt += 1
#
#
#         if cnt == (M**2):
#             return 1
#         else:
#             return 0
#
#

def check(i,j):
    global pArr, arr, cnt, M
    if pArr[0][0] == arr[i][j]:
        flag = 0
        for x in range(M): #패턴행
            for y in range(M): #패턴열
                    if pArr[x][y] != arr[i+x][j+y]:
                        return 0
        return 1





N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input())))
M = int(input())
pArr = []
for i in range(M):
    pArr.append(list(map(int, input())))

sol = 0
for i in range(N-M+1): #모눈종이의 시작행 제어
    for j in range(N-M+1): #모눈종이의 시작열 제어
        cnt = 0
        if check(i,j) == 1: #패턴 체크
            sol += 1

print(sol)