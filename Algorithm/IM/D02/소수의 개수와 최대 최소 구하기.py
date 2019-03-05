import sys
sys.stdin = open("소수의 개수와 최대 최소 구하기.txt")
a,b = map(int, input().split())
stack = []
for N in range(min(a,b), max(a,b)+1):
    cnt = 0
    flag = 0
    if N % 2 == 0 or N == 2:
        for i in range(1,N+1, 2):
            if N % i == 0:
                cnt += 1
            if cnt > 2:
                break

        if cnt == 2:
            stack += [N]
print(len(stack))
print(max(stack)+min(stack))