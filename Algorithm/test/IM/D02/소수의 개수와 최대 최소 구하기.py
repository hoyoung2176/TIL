import sys
sys.stdin = open("소수의 개수와 최대 최소 구하기.txt")

def gumsa(N):
    if N < 2:
        return False
    if N == 2:
        return True
    if N % 2 == 0:
        return False

    l = round(N ** 0.5) +1
    for i in range(3, l, 2):
        if N % i == 0:
            return False
    return True
    #
    # if N % 2 != 0 or N == 2:
    #     for i in range(3, N, 2):
    #         if N % i == 0:
    #             cnt += 1
    #         if cnt > 1:
    #             break
    #     if cnt == 0:
    #         stack += [N]


a,b = map(int, input().split())
stack = []
min_num = min(a,b)
max_num = max(a,b)


for N in range(min_num, max_num + 1):
    cnt = 0
    flag = 0
    if gumsa(N) == True:
        stack.append(N)


print(len(stack))
print(max(stack)+min(stack))