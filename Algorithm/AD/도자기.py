def DFS(start, cnt):
    global sol
    if cnt == M:
        for i in range(cnt):
            print(rec[i], end=' ')
        print()
        sol += 1
        return
    back = 0    #지역변수를 이용하여 기록하기
    for i in range(start, N):   #흙의 재료
        # if rec[cnt] == temp[i]: continue        #같은 재료이면 스킵
        # rec[cnt] = temp[i]
        if back == temp[i]: continue
        back = temp[i]
        DFS(i+1, cnt+1)
    rec[cnt] = 0

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    temp = list(map(int, input().split()))
    temp.sort()
    rec = [0]*N
    sol = 0
    DFS(0,0)
    print(sol)

# 카운팅방식으로 풀기
# def pick(n, r, p):
#     global cnt
#     if r>=M:
#         cnt += 1
#         return
#     if n>=N: return
#     for i in range(p, 26):
#         if not kind[i]: continue
#         kind[i] -= 1
#         pick(n+1, r+1, i)
#         kind[i] += 1
#
# for tc in range(int(input())):
#     N, M = map(int, input().split())
#     sand = list(map(int, input().split()))
#     kind = [0]*26
#     for i in sand:
#         kind[i-1] += 1
#     cnt = 0
#     pick(0, 0, 0)
#     print(cnt)