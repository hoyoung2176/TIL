def DFS(no, Lsum, Rsum):
    global sol
    if sol == 1:            # 가지치기
        return
    if Lsum == Rsum:        # 양쪽 저울의 무게가 같으면 성공
        sol = 1
        return
    if no >= CN:
        return

    DFS(no+1, Lsum+chu[no], Rsum)       # 현재 추를 왼쪽에 올리기
    DFS(no + 1, Lsum, Rsum + chu[no])   # 현재 추를 오른쪽에 올리기
    DFS(no + 1, Lsum, Rsum)             # 현재 추를 안 올리기
    # 현재 추를 사용하거나(왼쪽 또는 오른쪽 저울에 사용) 사용하지 않기
    # 양쪽저울 무게가 같으면 성공


# main -------------
CN = int(input())
chu= list(map(int, input().split()))
BN = int(input())
ball = list(map(int, input().split()))
rec = [0] * CN      # 기록 배열

for i in range(BN):
    sol = 0
    DFS(0, ball[i], 0)      # 0 번 추부터 시작, 왼쪽 저울 무게를 초기값으로, 오른 저울 무게 0
    if sol:
        print('Y', end=" ")
    else:
        print('N', end=" ")
print()

