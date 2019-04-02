import sys
sys.stdin = open("최소 신장 트리.txt")

T = int(input())

# #
# def findSet(x):
#     if x == p[x]:
#         return x
#     else:
#         return findSet(p[x])
#
# def mst():
#     global V
#     c = 0   #간선의 갯수
#     s = 0   #가중치 합
#     i = 0   #제어변수
#     while c < V:                    # MST 구성을 위해 B개 의 간선을 선택
#         p1 = findSet(edge[i][0])        #두 노드 대표원소 알아내기
#         p2 = findSet(edge[i][1])
#         if p1 != p2:                #사이클이 생성되지 않으면
#             s += edge[i][2]         #MST에 포함되므로 가중치 추가
#             c += 1                  # 간선 개수 증가
#             p[p2] = p1              # 대표 원소 관리 (union)
#         i += 1                      # 저장된 다음 간선으로 이동
#
#     return s
#
# for tc in range(1, T+1):
#     V, E = map(int,input().split())
#
#     edge = [list(map(int, input().split())) for _ in range(E)]
#
#     edge.sort(key=lambda t: t[2])
#     p = list(range(V+1))                    #대표원소 초기화(make set)
#     print("#{} {}".format(tc,mst()))



# Prim
def mst():
    global V
    total = 0
    u = 0
    D[u] = 0
    PI[u] = 0

    for i in range(V+1):
        min = 0x7fffffff
        for v in range(V+1):
            if visit[v] == 0 and min > D[v]:
                min = D[v]
                u = v

        visit[u] = 1
        total += adj[PI[u]][u]

        for v in range(V+1): # 인접한 정점 업데이트
            if adj[u][v] != 0 and visit[v] == 0 and adj[u][v] < D[v]:
                D[v] =adj[u][v]
                PI[v] = u
    return total

for tc in range(1, T+1):
    V, E = map(int,input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    D = [987654321] * (V+1)
    PI = list(range(V+1))
    visit = [0] *(V+1)

    #인접행렬로 만들기
    for i in range(E):
        edge = list(map(int, input().split())) #시작, 끝, 가중치
        for j in range(len(edge)):
            adj[edge[0]][edge[1]] = edge[2]     #방향성 없음
            adj[edge[1]][edge[0]] = edge[2]

    print('#{} {}'.format(tc,mst()))
