import sys
sys.stdin = open("호수의 깊이.txt")
#
# def find(i,j):
#     global arr
#     # 왼쪽의 육지까지 몇칸인지 확인
#     for k in range(i + 1):
#         if arr[i - k][j] == 0:
#             break
#     Lcnt = i - (i - k)
#
#     # 오른쪽 육지까지 몇칸인지 확인
#     for k in range(i + 1, N):
#         if arr[k][j] == 0:
#             break
#     Rcnt = k - i
#
#     # 위쪽 육지까지 몇칸인지 확인
#     for k in range(j + 1):
#         if arr[i][j - k] == 0:
#             break
#     Ucnt = j - (j - k)
#
#     # 아래쪽 육지까지 몇칸인지 확인
#     for k in range(j + 1, N):
#         if arr[i][k] == 0:
#             break
#     Dcnt = k - j + 1
#
#     arr[i][j] = min(Lcnt, Rcnt, Ucnt, Dcnt)

def find(i, j):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for dep in range(1, N):
        for k in range(4):
            if arr[i+dep*dr[k]][j+dep*dc[k]] == 0:
                return dep


N =int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    arr[i]=list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            ans += find(i,j)

print(ans)

# arr=[]
# for i in range(N):
#     arr.append(list(map(int, input())))