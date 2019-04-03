#중복순열
def DFS1(no):
    if no > N:
        for i in range(N):
            print(rec[i], end=" ")
        print()
    for i in range(1, 7):   # 눈
        chk[i] = 1
        rec[no] = i

#중복조합
def rptcomb(no, start):
    if no >= N:
        for i in range(N):
            if chk[i] == 1:
                print(i, end=" ")
        print()
        return
    for i in range(start, 7):   # 눈
        rec[no] = i     # 눈 기록
        rptcomb(no+1, i)


# 순열
def perm(no):
    if no >= N:
        for i in range(N):
            print(rec[i], end=" ")
        print()
        return
    for i in range(1, 7):
        if chk[i]:
            continue
        chk[i] = 1
        rec[no] = i # 눈 기록
        perm(no+1)
        chk[i] = 0

#조합
def comb(no, start):
    if no >= N:
        for i in range(N):
            if chk[i] == 1:
                print(i, end=" ")
        print()
        return
    for i in range(start, 7):   # 눈
        rec[no] = i     # 눈 기록
        rptcomb(no+1, i+1)







N, M = map(int, input().split())
chk = [0] * 7
rec = [0] * N
perm(0)
# M = 1 중복 순열

# M = 3 순열

# M = 2 중복 조합