def upperSearch2(s, e, data):
    sol = -1
    while s <= e:
        m = (s + e) // 2
        # data보다 작은값 중에서 가장 큰 값의 위치 찾기
        # data보다 작으면 오른쪽 영역 재탐색
        if arr[m] < data:
            s = m+1
            sol = m
        # 아니면 (크거나 같으면 ) 왼쪽 영역 재탐색
        else:
            e = m - 1
    return sol  # 못찾았으므로 return -1

#main-------------------
N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort()
cnt = 0
for i in range(N - 2):        # 첫번째 위치 고르기
    for j in range(i + 1, N - 1):
        # 두 번째 위치 고르기
        start = arr[j] + (arr[j] - arr[i])
        end = arr[j] + (arr[j] - arr[i]) *2
        cnt += upperSearch2(j, N - 1, end + 1) - upperSearch2(j, N - 1, start)

print(cnt)



# # DFS로 풀면 시간 오버됨.
# def DFS(no, start, cnt, d):
#     global sol
#     if no >= 3:
#         # for i in range(3):
#         #     print(chk[i], end=" ")
#         # print()
#         sol += 1
#         return
#     for i in range(start, N):
#
#         if no == 0:
#             chk[no] = temp[i]
#             DFS(no + 1, i + 1, temp[i], 0)
#         elif no == 1:
#             chk[no] = temp[i]
#             DFS(no + 1, i + 1, temp[i], temp[i])
#         elif temp[i] >= 2*d:
#             chk[no] = temp[i]
#             DFS(no+1, i + 1, temp[i], temp[i]-d)
#
#
# N = int(input())
# temp = []
# for i in range(N):
#     temp.append(int(input()))
# chk = [0] * 3
# sol = 0
# temp.sort()
# DFS(0, 0, 0, 0)
# print(sol)