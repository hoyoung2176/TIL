#선행조건을 리스트를 이용해 스택을 쌓아서 만든다.
import sys
sys.stdin = open("작업순서.txt")
# sys.stdin = open("test.txt")
T = 10

# DPS_route로 경로 찾기
def DPS_route():
    global visited, test, V
    stack=[]
    start(stack)
    # test>1이면 선행조건이 있으므로 새로운 시작점 찾기
    # if sum(test[S]) > 1:
    #     start()
    # else:
    while len(stack) != 0:
        t = stack.pop()
        print(t, end=' ')
        for k in range(1, V + 1):
            if test[t][k] == 1:
                visited[k] -= 1
                if visited[k] == 0:
                    stack.append(k)
                # DPS_route(k)
            # elif k == V and test[V][S] == 0:
            #     DPS_route(S+1)


#시작점 찾기
def start(stack):
    global test
    for S in range(1, len(test)):
        #시작점 test[S] == 0 이면서 test[x][S] == 0인 존재를 예외처리
        if visited[S] == 0:
            return stack.append(S)

for tc in range(T):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))
    test = [[0 for _ in range(V+1)] for _ in range(V+1)]


    visited = [0 for _ in range(V+1)]

    a = [0]


    #인접행렬

    for i in range(E):
        test[data[2*i]][data[2*i+1]] = 1
        visited[data[i*2+1]] += 1

    #스타트지점 S 찾기
    # start()
    print("#{}".format(tc + 1), end=" ")
    DPS_route()
    # for v in range(len(stack)):
    #     print(stack[v], end=" ")
    print()

