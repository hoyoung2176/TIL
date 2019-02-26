def process_solution(a,k):
    for i in range(1,k+1):
        if a[i] :
            print(data[i], end=" ")
    print()

def make_candidates(a, k,input, c):
    c[0] = True
    c[1] = False
    return 2

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
data = [0, 1, 2, 3]
a = [0] * NMAX   #부분집합 저장장소
backtrack(a, 0, 3)