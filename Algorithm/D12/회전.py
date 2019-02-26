import sys
sys.stdin = open('회전.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    queue = []
    i = 0
    
    #M번 회전하면서 큐에 맨 앞의 값을 추출해서 맨뒤에 넣는 작업반복.
    while i < M:
        i += 1
        queue = data.pop(0)
        data.append(queue)
        queue = []

    print("#{} {}".format(tc+1, data[0]))