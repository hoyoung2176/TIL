n = int(input())
temp = [list(map(int, input().split())) for _ in range(n)]
chk = [0]*n
rec = [0]*n         #비용 기록공간
b = [0]*n
min_sol = 1000000000
def DFS(no, hap):
    global min_sol
    if hap > min_sol:
        return
    if no == n:
        if sum(rec) < min_sol:
            min_sol = sum(rec)
        return
    for i in range(n):

        if chk[i]:
            continue
        chk[i] = 1
        rec[no] = temp[no][i]
        DFS(no+1, hap+temp[no][i])
        chk[i] = 0

DFS(0, 0)
print(min_sol)