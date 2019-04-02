


import sys
sys.stdin = open("최소 이동 거리.txt")

def getMinIdx():
    minV = 999999
    minIdx = 0
    for i in range(N+1):
        if visit[i] == 0 and D[i] < minV:
            minIdx = i
            minV = D[i]

    return minIdx


def dijkstra(goal):
    D[0] = 0               #출발점의 선가중치

    for i in range(N+1):
        if adj[0][i]:
            D[i] = adj[0][i] # D 초기화
    visit[0] = 1                #시작노드

    while True:
        node = getMinIdx()
        visit[node] = 1         #D가 가장 작은 노드 방문처리
        if node == goal:        #도착지에 도달하면
            return D[goal]

        for x in range(N+1):
            if adj[node][x]:       #minIdx 에 인접한 노드에 대해
                if D[x] > (D[node] + adj[node][x]):     # minIdx를 경유하는 비용
                    D[x] = D[node] + adj[node][x]       # D[x] 갱신



T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    adj = [[0 for _ in range(N+1)] for _ in range(N+1)]
    visit = [0] * (N+1)     #방문 처리
    D = [9999999999] * (N+1)    # 0번부터의 거리(가중치)

    for i in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = w


    print('#{} {}'.format(tc, dijkstra(N)))


