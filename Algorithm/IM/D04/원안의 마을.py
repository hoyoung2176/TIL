import sys, math
sys.stdin = open("원안의 마을.txt")

def find(x1,y1):
    global max_num
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                x2 = i+1
                y2 = j+1
                x = (x2-x1)**2
                y = (y2-y1)**2
                # 모듈 사용하는 경우
                # ans = math.ceil((x+y)**0.5)
                # 모듈 안쓸때
                ans = x + y
                k = 0
                while True:
                    k += 1
                    if ans<=k**2:
                        ans = k
                        break

                if ans <= 13 and ans >= 1:
                    if max_num < ans:
                        max_num = ans




N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input()))

max_num = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            x1 = i+1
            y1 = j+1
            find(x1, y1)

print(max_num)
