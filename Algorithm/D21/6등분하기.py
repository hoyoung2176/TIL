def perm
    global ans
    if sum > ans:
        return
    if k == N:
        if ans > sum:
            ans = sum
    else:
        for i in range(k,N):
            A[k],A[i] = A[i], A[k]
            perm(n, k+1, sum +dist())