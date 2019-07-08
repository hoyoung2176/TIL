
#현재 군함반경이내 모든 군함에너지 차감 함수
def clear(i):
    global arr
    for j in range(N):
        temp = abs(arr[j][0] - arr[i][0]) + abs(arr[j][1] - arr[i][1])
        if temp <= R:
            arr[j][2] -= P

#현재 군함반경이내 모든 군함에너지 복원 함수
def update(i):
    global arr
    for j in range(N):
        temp = abs(arr[j][0] - arr[i][0]) + abs(arr[j][1] - arr[i][1])
        if temp <= R:
            arr[j][2] += P

def DFS(no):        #현재 no  미사일을 모든 군함에 쏘아보는 경우의 수 시도
    global sol
    if no == M:
        cnt = 0     #남아있는 군함의 갯수
        for i in range(N):
            if arr[i][2] > 0:
                cnt += 1

        if cnt < sol:
            sol = cnt
        return

    for i in range(N):  #군함
        if arr[i][2] <= 0:      #군함이 침몰하지 않는 군함에서만 시도
            continue
        clear(i)    # 현재 군함반경이내 모든 군함에너지 차감
        DFS(no+1)   # 다음 미사일로
        update(i)   # 현재 군함반경이내 모든 군함에너지 복원


#main----------------

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]      # 열, 행, 에너지
M, P, R = map(int, input().split())     # 미사일 개수, 파워, 범위
sol = 16

DFS(0)
print(sol)
