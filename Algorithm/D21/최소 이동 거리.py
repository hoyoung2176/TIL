import sys
sys.stdin = open("최소 이동 거리.txt")

def dijkstra(N, E, graph):
    U = [N]

    for i in range(N):
        D[i] =


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    temp = []
    for i in range(E):
        temp.append(list(map(int, input().split())))

    #인접행렬만들기
    data = [[10000000000000000000000 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(E):
        data[temp[i][0]][temp[i][1]] = temp[i][2]
        data[temp[i][0]][temp[i][0]] = 0
    data[N][N] = 0





    dijkstra(0, E, data)

