import sys
sys.stdin = open("color.txt")
T = int(input())
for tc in range(T): #테스트 케이스
    N =int(input())
    cnt = 0
    arr = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(N): #색칠 해야하는 수
        r1,c1,r2,c2,color=list(map(int,input().split()))

        for x in range(r1, r2+1):
            for y in range(c1,c2+1):
                arr[x][y] += color
                if arr[x][y] == 3:
                    cnt += 1


    print("#{} {}".format(tc+1, cnt))