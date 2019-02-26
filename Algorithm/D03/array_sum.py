import sys
sys.stdin = open("array_sum.txt")
T = 10

for tc in range(T):
    N = int(input())
    arr = [[0 for j in range(100)] for k in range(100)]
    test = []
    for i in range(100):
        arr[i] = list(map(int, input().split()))

    for x in range(len(arr)):
        sum_weight = 0
        diag = 0
        back_diag = 0
        for y in range(len(arr[x])):
            sum_weight += arr[x][y]
            test.append(sum_weight)
            if x==y:
                diag += arr[x][y]
                test.append(diag)
            if x+y == 100:
                back_diag += arr[x][y]
                test.append(back_diag)


    for y in range(len(arr[x])):
        sum_height = 0
        diag = 0
        for x in range(len(arr)):
            sum_height += arr[x][y]
            test.append(sum_height)
    ans = max(test)
    print("#{} {}".format(tc + 1, ans))





    # print(arr)
    # for x in range(len(arr)):
    #     sum_weiht = 0
    #     for y in range(len(arr[x])):
    #         sum_weiht +=arr[x][y]
    #         test.apped(sum_weiht)

    # print(test)


    #
    #
    # arr = list(map(int, input().split()))
    # for x in range(len(arr)):
    #     for y in range(len(arr[x])):
    #         print(arr[x][y], end=" ")


# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         print(arr[i][j], end = " ")
#     print()
# print()
#
#
#
#
# for tc in range(T):
#     N = int(input())
#     data = list(map(int, input().split()))
#     ans = 0
#     max_num = data[0]
#     min_num = data[0]
#
#
#
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         print(arr[i][j], end = " ")
#     print()
# print()
#
# print("#{} {}".format(tc + 1, ans))
