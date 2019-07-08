import sys
sys.stdin=open('스파이조직.txt')

N, temp = input().split()
N=int(N)
temp = list(temp)
arr = [[] for _ in range(51)]
i = 0
while len(temp) != 0:
    a = temp.pop(0)
    if a == '<':
        i += 1
    elif a == '>':
        i -= 1
    else:
        b = temp.pop(0)
        while b != '<':
            a = a+b
            b = temp.pop(0)
        temp = [b] + temp
        arr[i] += [int(a)]

print(*arr[N])

