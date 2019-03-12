def repeated_combination(n, k, q):
    if k == 0:
        myprint(q)
    else:
        if n == 0:                              # n이 0보다 작아지면 안되므로
            return
        else:
            T[k-1] = A[n-1]                     # data A에 있는 n에 있는 것을 결과 T에 넣는다
            repeated_combination(n, k - 1, q)   # n이 포함된 경우
            repeated_combination(n - 1, k, q)   # n이 포함 안된 경우


def myprint(q):
    while q != 0:
        q -= 1
        print("%d" % (T[q]), end=' ')
    print('')

A = [1, 2, 3, 4]
T = [0, 0, 0]
n = 4
k = 3
q = 3
repeated_combination(n, k, q)