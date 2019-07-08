# 이진 탐색을 이용하여 예산분배 하는 방법
def check(m):
    # 상한액으로 지방에서 요청액을 배정 가능하면 배정, 아니면 상한액으로 합계 계산
    tot = 0
    for i in range(N):
        if m > temp[i]:
            tot += temp[i]
        else:
            tot += m
    if tot <= M:
        return 1
    else:
        return 0

# main ----------------
N = int(input())
temp = list(map(int, input().split()))
M = int(input())

s, e = 1, max(temp)
sol = 0

# 1원부터 max원까지 상한가를 mid 값으로 결정하여 총액 이하면 상한액 증가, 아니면 감소
while s <= e:
    m = (s+e)//2
    if check(m):        # 예산 분배에 성공하면 상한액 증가
        sol = m
        s = m + 1
    else:               # 예산 분배에 실패하면 상한액 감소
        e = m - 1
print(sol)