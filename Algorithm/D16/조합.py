def combination(n, k, q):
    if k == 0:
        myprint(q)
    else:
        if n < k:  #중복 불가능
            return
        else:
            T[k-1] = A[n-1] # data A에 있는 n에있는 것을 결과 T에 넣는다
            combination(n - 1, k - 1, q)  # n이 포함된 경우
            combination(n - 1, k, q) #n이 포함 안된 경우


def myprint(q):
    while q != 0:
        q -= 1
        print("%d" % (T[q]), end=' ')
    print('')

def comb(n, k, q):
    if k == 0:
        myprint(q)
    else:
        if n < k:  #중복 불가능
            return
        else:
            return combination(n - 1, k - 1, q) + combination(n - 1, k, q)
a=[]
a += [i for i in range(1,52)]
T = [0, 0, 0]
n = 52
k = 5
q = 3
combination(n, k, q)
print(comb(n, k, q))

# dp
def comb(n,r):
    memo = [[0 for _ in range(n+1)]]
    for i in range(n+1):
        for j in range(min(i,r)):
            if j == 0 or j == i:
                memo[i][j] = 1
            else:
                memo[i][j] = memo[i-1][j-1] + memo[i-1][j]
        return memo[n][r]