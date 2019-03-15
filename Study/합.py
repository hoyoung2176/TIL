import sys
sys.stdin = open("합.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    temp = list(map(int, input().split()))
    result = 0
    ans = 0
    for i in range(len(temp)):
        result += temp[i]
        if result <= 0:
            result = 0
        if ans < result:
            ans = result

    print("#{} {}".format(tc+1, ans))