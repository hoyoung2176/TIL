import sys
sys.stdin = open('폭탄돌리기.txt')


M = 8
boom = 210
K = int(input())
N = int(input())
for i in range(N):
    T, result = map(str, input().split())
    boom -= int(T)
    if boom > 0:
        if result == 'T':
            if K < 8:
                K += 1
            elif K == M:
                K = 1
    else:
        break



print(K)