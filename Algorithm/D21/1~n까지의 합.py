def calc(N):
    global ans
    if N == 1:
        return 1
    else:

        return N + calc(N - 1)

ans = 0
N = int(input())
print(calc(N))
