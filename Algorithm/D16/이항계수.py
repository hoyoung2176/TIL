def bino2(n,k):
    global B[][]
    for i in range(n+1):
        for j in range(min(i, k)):
            if j = 0 or j = i:
                B[i][j] = 1
            else:
                B[i][j] = B[i-1][j-1] + B[i-1][j]
    return B[n][k]