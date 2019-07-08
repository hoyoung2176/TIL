#루프를 이용한 체크방법
dr = [-1, -1, -1]
dc = [-1, 0, 1]
def check(r, c):
    # 현재 좌표에 퀸을 놓을 수 있는지 여부 체크
    for i in range(3):  #3방향
        for k in range(1, N): # 1배, 2배 ....  증감치의 배수 계산
            nr = r + (dr[i]*k)
            nc = c + (dc[i]*k)
            if nr<0 or nr >=N or nc<0 or nc >=N:
                break
            if arr[nr][nc] == 1:        #놓을 수 없음 실패
                return 0
    return 1                # 퀸 놓을 수 있음 성공

def DFS(no):
    # 현재 행에서 모든 열에 퀸을 놓아보는 경우
    global sol
    if no >= N:
        sol += 1
        return

    # 체크 배열을 이용한 풀이(속도가 빠르다)
    for i in range(N):
        if chk1[i]:     # 세로방향 체크
            continue
        if chk2[no + i]:     # 오른쪽 대각선방향 체크
            continue
        if chk3[(N - 1) - (no - i)]:     # 왼쪽 방향 대각선방향 체크
            continue
        chk1[i] = chk2[no + i] = chk3[(N - 1) - (no - i)] = 1
        DFS(no+1)
        chk1[i] = chk2[no + i] = chk3[(N - 1) - (no - i)] = 0

    # #루프를 이용해 확인
    # for i in range(N):
    #     if check(no, i): #퀸을 놓을 수 없으면
    #         arr[no][i] = 1  #퀸 놓기
    #         DFS(no + 1)
    #         arr[no][i] = 0  #퀸 빼기

N = int(input())
arr = [[0]*N for _ in range(N)]
sol = 0

chk1 = [0]*N        # 위에 퀸있는지 확인함
chk2 = [0]*N*2        # 우 대각선 퀸 있는지 체크
chk3 = [0]*N*2        # 좌 대각선 퀸 있는지 체크

DFS(0)
print(sol)