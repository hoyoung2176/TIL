def check(no, color):
    # 현재노드와 연결된 노드중 중복색상 체크
    for i in range(no): # 연결된 노드(열)
        if arr[no][i] == 1 and rec[i] == color: # 연결된 노드와 같은 색이면 실패
            return 0
    return 1

def DFS(no):
    global flag, rec
    if flag:
        return
    if no >= N:         # 끝까지 색칠할 수 있으면 성공
        flag = 1
        return
    # 현재 노드에게 1~M 색상을 칠해 보는 경우의 수
    for i in range(1, M+1):
        if check(no, i):    # 현 노드에게 칠할수 있으면 기록하고 다음노드로
            rec[no] = i     # 색상 기록
            DFS(no+1)
            if flag:
                return

# main -----------------
N, M = map(int, input().split())
rec = [0]*N     # 색상 기록
arr = []        # 인접 행렬
for i in range(N):      # 0행 0열부터 사용
    arr += [list(map(int, input().split()))]

flag = 0
DFS(0)      # 첫 번째 노드부터 시작

if flag:    # 성공
    for i in range(N):
        print(rec[i], end=' ')
else:
    print(-1)   # 실패