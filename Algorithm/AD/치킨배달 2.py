def solve():
    # M개 골랐을때 고른치킨과의 최소인 거리의 합 비교
    hap = 0
    for i in range(HN):                             # 현재 집에서 고른 치킨집과 최소인 거리 찾기
        dist_min = 20000000
        for j in range(CN):                         # 치킨집
            if not sel[j]: continue                 # 선택안한 치킨집이면 스킵
            dist_min = min(dist_min, arr[j][i])     # 최소거리 비교
        hap += dist_min
    return  hap

def DFS(no, cnt):
    # 현재 치킨집을 고르거나 고르지 않는 경우 시도
    global sol
    if cnt == M:
        hap = solve()
        if hap < sol:
            sol = hap
        return
    if no >= CN:
        return
    sel[no] = 1
    DFS(no + 1, cnt+1)
    sel[no] = 0
    DFS(no + 1, cnt)

# main -------------------------------------
N, M = map(int, input().split())
temp = [list(map(int, input().split())) for _ in range(N)]
house = []
chk = []
for i in range(N):
    for j in range(N):
        if temp[i][j] == 2:
            chk.append((i,j),)
        elif temp[i][j] == 1:
            house.append((i,j),)
HN = len(house)
CN = len(chk)
arr = [[0 for _ in range(HN)] for _ in range(CN)]
for i in range(CN):
    for j in range(HN):
        dist= abs(chk[i][0] - house[j][0]) + abs(chk[i][1] - house[j][1]) #치킨집과 집과의 거리
        arr[i][j] = dist

sel = [0] *HN
sol = 1000000000
DFS(0, 0)
print(sol)
