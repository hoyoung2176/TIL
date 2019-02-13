#선행조건을 리스트를 이용해 스택을 쌓아서 만든다.
import sys
sys.stdin = open("작업순서.txt")
# sys.stdin = open("test.txt")
T = 10

# def pop():
#     if len(stack) == 0:
#         print("Stack is Empty!")
#         return
#     else:
#         return stack.pop(-1)

# DPS_route로 경로 찾기
def DPS_route(S):
    global E, visited, test, V, stack, x, y

    # test>1이면 선행조건이 있으므로 새로운 시작점 찾기
    # if sum(test[S]) > 1:
    #     start()
    # else:
        for k in range(1, V + 1):
            if visited[k] == 0 and test[k][S] == 1 and sum(test[k]) < 2:
                visited[k] = 1
                test[k][S] -= 1
                stack.append(S)
                DPS_route(k)
            elif k == V and test[V][S] == 0:
                DPS_route(S+1)


#시작점 찾기
def start():
    global test, x, y
    for S in range(1, len(test)):
        #시작점 test[S] == 0 이면서 test[x][S] == 0인 존재를 예외처리
        if S not in visited and max(test[S]) == 0:
            return DPS_route(S)

for tc in range(T):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))
    test = [[0 for _ in range(V+1)] for _ in range(V+1)]

    #x가 입력 y가 출력
    x = []
    y = []
    visited = [0 for _ in range(V+1)]
    stack=[]
    a = [0]


    #인접행렬
    for j in range(len(data)):
        if j % 2:
            x.append(data[j])
        else:
            y.append(data[j])


    for i in range(len(x)):
        test[x[i]][y[i]] = 1

    #스타트지점 S 찾기
    start()
    print("#{}".format(tc + 1), end=" ")
    for v in range(len(stack)):
        print(stack[v], end=" ")
    print()

