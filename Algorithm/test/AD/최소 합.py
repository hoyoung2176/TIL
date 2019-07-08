def comb(no, hap):
    global sol1
    if sol1 < hap:
        return

    if no >= N:
        if sol1 > hap:
            sol1 = hap
        return
    for i in range(N):
        comb(no+1, hap+arr[no][i])

def recomb(no, start, hap):
    global sol2, rec
    if sol2 < hap:
        return

    if no >= N:
        # for i in range(N):
        #     print(rec[i], end=" ")
        # print()
        if sol2 > hap:
            sol2 = hap
        return
    for i in range(N):
        if rec[i]:
            continue
        rec[i] = arr[no][i]
        recomb(no + 1, i+1, hap + arr[no][i])
        rec[i] = 0

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
sol1 = 10000000000
sol2 = 10000000000
rec = [0]*N
comb(0, 0)
recomb(0, 0, 0)
print(sol1)
print(sol2)