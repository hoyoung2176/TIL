def fibo(N):
    global ans
    if N < 3:
        return 1
    elif N not in memo:
        memo[N] = fibo(N - 1) + fibo(N - 2)
    return memo[N]

N = int(input())
memo = [0] * (N+1)
print(fibo(N))