import sys
sys.stdin = open('contact.txt')

def bfs(S):
    global visited, arr
    queue = []
    queue.append(S)
    while len(queue) != 0:
        S = queue.pop(0)
        for i in arr[S]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[S] + 1



T = 10
for tc in range(T):
    #N은 인원수 S는 시작하는 사람
    N, S = map(int, input().split())
    arr = [[] for _ in range(N + 1)]
    visited = [0 for _ in range(N + 1)]
    data = list(map(int, input().split()))
    ans = 0
    for i in range(0, N, 2):
        arr[data[i]] += [data[i+1]]
    bfs(S)
    for i in range(N+1):
        if visited[i] == max(visited):
            ans = i

    print("#{} {}".format(tc+1, ans))
