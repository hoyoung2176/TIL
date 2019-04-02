import sys
sys.stdin = open("그룹나누기.txt")

def findset(n):
    while parent[n] != n:
        n = parent[n]
    return n

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    parent = list(range(N+1))       # 대표원소 초기화
    temp = list(map(int, input().split()))
    for j in range(M):
        parent[findset(temp[2*j+1])] = findset(temp[2*j])

    cnt = 0
    for i in range(len(parent)):
        if parent[i] == i:
            cnt += 1

    print('#{} {}'.format(tc, cnt-1))