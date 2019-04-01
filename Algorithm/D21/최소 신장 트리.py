import sys
sys.stdin = open("최소 신장 트리.txt")

T = int(input())


def findSet(x):
    if x == p[x]:
        return x
    else:
        return findSet(p[x])

def mst():
    global V
    c = 0   #간선의 갯수
    s = 0   #가중치 합
    i = 0   #제어변수
    while c < V:
        p1 = findSet(edge[i][0])
        p2 = findSet(edge[i][1])
        if p1 != p2:                #사이클이 생성되지 않으면
            s += edge[i][2]
            c += 1
            p[p2] = p1
        i += 1
    return s

for tc in range(1, T+1):
    V, E = map(int,input().split())

    edge = [list(map(int, input().split())) for _ in range(E)]

    edge.sort(key=lambda t: t[2])
    p = list(range(V+1))
    print("#{} {}".format(tc,mst()))