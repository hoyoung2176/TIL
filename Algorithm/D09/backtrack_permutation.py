# 순열 backtrack, TSP 문제에 자주쓰임 도시를 뺑뺑 돌고 출발지로 돌아오는데 가장 짧은 루트문제 등
def process_solution(a, k):
    for i in range(1, k+1):
        print(data[a[i]], end=" ")
    print()

def make_candidates(a, k, input, c):
    in_perm = [False] * NMAX

    for i in range(1, k):
        in_perm[a[i]] = True

    ncands = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncands] = i
            ncands += 1
    return ncands

def backtrack(a, k, input):
    global  MAXCANDITATES
    c = [0] * MAXCANDITATES

    if k == input:
        process_solution(a,k)

    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]
            backtrack(a, k, input)


MAXCANDITATES = 100  #적당한 숫자 입력
NMAX = 100   #적당한 숫자 입력
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [0] * NMAX   #부분집합 저장장소
backtrack(a, 0, 10)