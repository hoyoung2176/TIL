import sys
sys.stdin = open('contact.txt')

#bfs
def bfs(S):
    global visited, arr
    queue = []
    queue.append(S)
    while len(queue) != 0:
        S = queue.pop(0)
        for i in arr[S]:
            #연락 받은지 여부 확인
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[S] + 1



T = 10
for tc in range(T):
    #N은 인원수 S는 시작하는 사람
    N, S = map(int, input().split())

    #연락 여부확인 리스트
    visited = [0 for _ in range(N + 1)]

    # 정답
    ans = 0

    # arr는 인접리스트, data는 외부 정보를 임시로 정보 받는 리스트
    arr = [[] for _ in range(N + 1)]
    data = list(map(int, input().split()))
    for i in range(0, N, 2):
        arr[data[i]] += [data[i+1]]

    #시작점을 이용하여 bfs(전화) 돌림
    bfs(S)

    # 전화가 끝나고 가장 마지막에 받은 사람들 중에 가장 큰 숫자를 가진 사람을 찾기
    for i in range(N+1):
        if visited[i] == max(visited):
            ans = i

    print("#{} {}".format(tc+1, ans))
