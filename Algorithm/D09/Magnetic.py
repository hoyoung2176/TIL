import sys
sys.stdin = open("Magnetic.txt")

T = 10
for tc in range(T):
    N = int(input())
    data = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0

    for i in range(N):
        data[i] = list(map(int, input().split()))

    for y in range(N):
        stack = []
        for x in range(N):
            if data[x][y] == 1:
                stack.append(data[x][y])
                if len(stack) > 1:
                    stack.pop()
            elif len(stack) == 1 and data[x][y] == 2:
                stack.pop()
                cnt+=1

    print("#{} {}".format(tc+1,cnt))