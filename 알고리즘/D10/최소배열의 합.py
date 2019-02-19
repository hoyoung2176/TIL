#순열 이용하여 풀기
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
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k) #답이면 원하는 작업을 한다.
    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]
            backtrack(a, k, input)
#
# def backtrack(a, k, N):
#     global ans
#     if k = N:
#         process_solution(a, k)
#     else:
#         k += 1
#         ncands = make_candidates(a, k, input, c)
#         for i in range(ncands):
#             a[k] = c[i]
#             backtrack(a, k, input)



import sys
sys.stdin = open("최소배열의합.txt")

T =int(input())
for tc in range(T):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    ans = 0
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    MAXCANDIDATES = 100
    NMAX = 100
    data = [0, 1, 2, 3]
    a = [0] * NMAX
    backtrack(a, 0, N)




