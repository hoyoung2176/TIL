import sys
sys.stdin = open('노드의 거리.txt')

#연결 안된것이 있을 수 있다.

def bfs(S):
    global arr, N, G
    queue = []
    # 큐에 시작점 저장 후 방문 표시
    queue.append(S)
    visited[S] = 1

    # 큐가 없을 때 까지 돌리기.
    while len(queue) != 0:
        #시작점을 큐에서 빼기
        S = queue.pop(0)
        for i in arr[S]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[S]+1

T = int(input())
for tc in range(T):

    #N은 노드의 수, M은 간선의 숫자
    N, M = map(int, input().split())

    #방문여부 확인용 리스트
    visited = [0 for _ in range(N+1)]

    #인접리스트
    arr = [[] for _ in range(N + 1)]
    for _ in range(M):
        data = list(map(int, input().split()))
        arr[data[0]] += [data[1]]
        arr[data[1]] += [data[0]]

    # S는 시작점 G는 도착점
    S, G = map(int, input().split())


    bfs(S)

    # 시작점을 visited[S]=1로 시작했기 때문에 1을 빼준다.
    if visited[G] > 0:
        print("#{} {}".format(tc+1, visited[G]-1))
    # 도착 노드로 도착하는 간선이 없는 경우 시작점
    else:
        print("#{} {}".format(tc + 1, visited[G]))

