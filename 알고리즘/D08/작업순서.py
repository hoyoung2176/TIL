#선행조건을 리스트를 이용해 스택을 쌓아서 만든다.
import sys
sys.stdin = open("작업순서.txt")

T = 1

# def push(item):
#     ans.append(item)
#
# def pop():
#     if len(ans) == 0:
#         return
#     else:
#         return ans.pop(-1)
#
def DPS_route(S):
    global E, visited, test, V, G
    for k in range(V + 1):
        if visited[k] == 0 and test[S][k] == 1 and test:
            visited[k] = 1
            DFS_route(k)


for tc in range(T):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))
    test = [[0 for _ in range(V+1)] for _ in range(V+1)]
    x = []
    y = []
    visited = [0 for _ in range(V+1)]
    for j in range(len(data)):
        if j % 2:
            x.append(data[j])
        else:
            y.append(data[j])
    for i in x:
        for j in y:
            test[i][j] = 1


    #스타트지점 S

    DPS_route()




    # #
    # # for j in range(len(G)):
    # #     if S[j] not in ans:
    # #         pop(S[j])
    #
    #
    # print("#{} {}".format(tc + 1, data))
