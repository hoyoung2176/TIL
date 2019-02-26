import sys
sys.stdin = open("sum_input.txt")
T = int(input())

for tc in range(T):
    n, sum_test = map(int, input().split())
    A = list(range(1, 13))
    countA = 0
    for i in range(1, 1 << len(A)):
        sum_arr = 0
        num = 0
        for j in range(len(A)):
            if i & (1 << j):
                sum_arr += A[j]
                num += 1
                # print(A[j], end = ", ")
        # print()
        # print("{} {}".format(num, sum_arr))
        if num == n and sum_arr == sum_test:
            countA += 1
    print("#{} {}".format(tc + 1, countA))
