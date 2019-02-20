import sys
sys.stdin = open("최소배열의합.txt")

T =int(input())

def process_solution(a, k):
    global result, ans, data, cnt
    result = 0
    for i in range(1, k+1):
        result += arr[i-1][data[a[i]]]

    if ans > result:
        ans = result
    cnt += 1

def make_candidates(a, k, input, c):
    in_perm = [False] * NMAX

    for i in range(1, k):
        in_perm[a[i]] = True

    ncands = 0
    for i in range(0, input):
        if in_perm[i] == False:
            c[ncands] = i
            ncands += 1
    return ncands

def backtrack(a, k, input):
    global MAXCANDIDATES, total_cnt
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k) #답이면 원하는 작업을 한다.
    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]

    total_cnt += 1

for tc in range(T):
    N = int(input())
    # data = [[0 for _ in range(N)] for _ in range(N)]
    MAXCANDIDATES = 100
    NMAX = 100
    ans = 1000000000000000000
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    data = [i for i in range(N)]
    a = [0] * NMAX
    result = 0
    cnt = 0
    total_cnt = 0
    sum = 0
    backtrack(a, 0, N)
    print("#{} {}".format(tc+1, ans))
    print(f'count:{cnt}')
    print(f'count:{total_cnt}')