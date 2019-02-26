#방향성있는 DFS 문제
import sys
sys.stdin = open("그래프경로.txt")

T = int(input())

def DFS_route(S):
    global E, visited, data, V, G
    for j in range(V+1):
        if visited[j] == 0 and data[S][j] == 1:
            visited[j] = 1
            DFS_route(j)

for tc in range(T):

    #노드의 개수(V)와 간선의 개수(E)
    V, E = map(int, input().split())

    #그래프 경로를 DATA라는 리스트를 이용하여 표현
    data = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(E):
        x, y = map(int, input().split())
        data[x][y] = 1

    #출발노드(S), 도착노드(G)
    S, G = map(int, input().split())

    #방문여부 확인
    visited = [0 for _ in range(V+1)]

    #재귀함수 불러오기
    DFS_route(S)

    #도착노드에 도착하는지 확인
    if visited[G]:
        result = 1
    else:
        result = 0

    print("#{} {}".format(tc+1, result))
