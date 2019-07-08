# BFS로 문제풀이

# 플로도필 기법 - 나와 연결되어있는 영역 찾는 재귀적 기법
def FF(no):
    # 현재 컴퓨터에서 방문 안한 연결된 컴퓨터를 따라가면서 방문표시하고 카운트
    global visited, cnt
    for i in range(1, N+1):
        if arr[no][i] == 1 and visited[i] == 0:
            cnt += 1
            visited[i] = 1
            FF(i)

N = int(input())            # 컴퓨터 번호
M = int(input())            # 연결되어 있는 쌍의 수

# 인접 행렬
arr = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    n1, n2 = map(int, input().split())
    arr[n1][n2] = 1         # 연결 체크
    arr[n2][n1] = 1

visited = [0]*(N+1)
visited[1] = 1
cnt = 0
FF(1)       # 1번 컴퓨터 부터 시작
print(cnt)
