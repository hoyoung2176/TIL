def comb(no, cnt, hap):
    global sol
    if cnt + (N - no) < N//2:
        return
    if cnt == N // 2:  # N / 2 개를 고른 경우만 길이의 차 비교
        temp = abs(hap - (tot - hap))  # 이등분 한 테이프의 차이
        if temp < sol:
            sol = temp
        return

    if no >= N:
        # for i in range(N): print(rec[i], end=' ')
        # print(cnt, hap)
        return

    # 현재 no번 테이프를 붙이거나 붙이지 않는 경우의 시도
    rec[cnt] = arr[no]
    comb(no+1, cnt+1, hap+arr[no])
    rec[cnt] = 0
    comb(no + 1, cnt, hap)


N = int(input())
arr = list(map(int, input().split()))
rec = [0]*N
sol = 500*20
tot = sum(arr)
comb(0, 0, 0)   # 0번째 테이프부터 시작, 고른개수 0개, 테이프 길이합
print(sol)