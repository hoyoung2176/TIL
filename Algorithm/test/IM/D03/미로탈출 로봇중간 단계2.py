import sys
sys.stdin = open("미로탈출 로봇중간 단계.txt")

N = int(input())
arr = [[1]*(N*2) for _ in range(N+2)]
for i in range(1,N+1):
    arr[i]= [1] + (list(map(int, input()))) + [1]
Darr = list(map(int,input().split()))

Dno = 0 #방향순서
dr = [0, 1, 0, -1, 0] #아래1 왼2 위3, 오른4 방향
dc = [0, -1, 0, 1]
r,c = 1, 1 #현재좌표
cnt = 0
while True:
    #좌표계산
    r = r + dr[Darr[Dno]]
    c = c + dc[Darr[Dno]]

    if arr[r][c] == 0: # 0이면
        #방문표시하고 카운트
        arr[r][c] = 9
        cnt += 1

    elif arr[r][c] == 1: # 1이면
        # 이전좌표로 이동하고 방향전환(단, 방향은 로테이션)
        r = r - dr[Darr[Dno]]
        c = c - dc[Darr[Dno]]
        Dno += (Dno+1) % 4        #4가 넘으면 초기화 된다.

    else:
        break # 지나간 자리이면 탈출
print(cnt)