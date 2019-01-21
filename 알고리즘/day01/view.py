import sys
sys.stdin = open("view_input.txt")
T = 10
for tc in range(10):
    ans = 0
    N = int(input())
    data = list(map(int, input().split()))
    ans_1 = 0
    # result = []
    #K, P = map(int,input().split()) 두개 받을때.
    # print(data)

    for i in range(2,N-2):

        #  if ans_1 > 0:
        #     ans += ans_1
        if data[i-2] < data[i] and data[i-1] < data[i] and data[i+2] < data[i] and data[i+1] < data[i]:
            ans_1 = data[i] - max(data[i - 2], data[i - 1], data[i + 1], data[i + 2])
            ans += ans_1








    print("#{} {}".format(tc+1, ans))