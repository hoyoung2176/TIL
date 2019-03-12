def PI(n, r, q):
    if r == 0:
        myprint(q)
    else:
        for i in range(n-1, -1, -1):
            a[i], a[n-1] = a[n-1], a[i]
            t[r-1] = a[n-1]
            PI(n, r-1, q)
            a[i], a[n - 1] = a[n - 1], a[i]

def myprint(q):
    while q != 0:
        q -= 1
        print("%d" % (t[q]), end=' ')
    print('')
t = [0]*10
a=[]
a += [i for i in range(1,11)]
PI(4, 3, 3)