import sys
sys.stdin = open("section_sum.txt")
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    ans = 0
    Max_sum = 0
    Min_sum = 99999999999999999999999 # min 바꾸기용
    sum_test = 0

    for i in range(N-1,N-(N-M+1)-1,-1): #거꾸로 N  까지의 범위 추출
        for j in range(M):
            sum_test += data[i - j]  #비교함수 누적
        if sum_test >= Max_sum: #비교함수와 비교하여 max와 min값 바꿈
            Max_sum = sum_test
        if sum_test <= Min_sum:
            Min_sum = sum_test
        sum_test = 0
    ans = Max_sum - Min_sum
    print("#{} {}".format(tc + 1, ans, sum_test))





    # for i in range(M):
    #     Min_sum += data[i]
    # for j in range(N-M,N):
    #     Max_sum += data[j]




