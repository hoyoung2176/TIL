import sys
sys.stdin = open("연습3_input.txt")
# 정점의 수와 간선의 개수
n, e = map(int, input().split())
n += 1
temp = list(map(int, input().split()))

#인접행렬을 통하여 입력값 받기
G = [[0 for i in range(n)] for j in range(n)]
visited = [0 for i in range(n)] #방문처리

for i in range(0, len(temp), 2 ): #입력
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

# for i in range(n):
#     print("{} {}".format(i, G[i]))

#v는 시작 정점
# 글로벌로 전역변수 처리하여 풀기

def dfs(v):
    global G, visited, n
    visited[v] = 1
    print(v, end = " ")

    for w in range(n):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

dfs(1)


