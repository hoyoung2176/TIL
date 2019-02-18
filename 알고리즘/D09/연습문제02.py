def process_solution(a,k):
    global cnt
    sum = 0
    for i in range(1,k+1):
        if a[i] :
            sum += data[i]

    if sum== 10:
        for i in range(1, k+1):
            if a[i]:
                print(data[i], end=" ")
        print()
    cnt += 1

def make_candidates(a, k,input, c):
    c[0] = True
    c[1] = False
    return 2

def backtrack(a, k, input):
    # 가지치는 방법은 이자리에 조건문으로 되돌려주거나 함수호출할때 조건문으로 함부로 호출하지 않게한다.

    global  MAXCANDITATES, total_cnt
    c = [0] * MAXCANDITATES

    if k == input:
        process_solution(a,k)

    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]
            backtrack(a, k, input)
    total_cnt += 1


MAXCANDITATES = 100
NMAX = 100
data = [i for i in range(11)]
a = [0] * NMAX
cnt = 0
total_cnt = 0
backtrack(a, 0, 10)
print(f'count:{cnt}')
print(f'count:{total_cnt}')
