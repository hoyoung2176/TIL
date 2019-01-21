#최대 최소의 차이값 구하기(max와 min 금지)
import sys
sys.stdin = open("min_max_input.txt")
T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    ans = 0
    max_num = data[0]
    min_num = data[0]
    for i in data: #data에 있는 것을 i에 넣어 판단.
        if i >= max_num: #max와 min을 i와 비교하여 바꾸기 합니다.
            max_num = i
        if i <= min_num:
            min_num = i

    ans = max_num - min_num
    print("#{} {}".format(tc + 1, ans))

# import sys
# sys.stdin = open("min_max_input.txt")
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     data = list(map(int, input().split()))
#     ans = 0
#     max_num = data[0]
#     min_num = data[0]
#     n = 1
#     for i in range(len(data)): #data에 있는 것을 i에 넣어 판단.
#         if data[i] >= max_num: #max와 min을 i와 비교하여 스왑합니다.
#             max_num = data[i]
#
#         if data[i] <= min_num:
#             min_num = data[i]
#
#         ans = max_num - min_num
#
#     print("#{} {}".format(tc + 1, ans))
#최대 최소의 차이값 구하기

#함수사용
# import sys
# sys.stdin = open("min_max_input.txt")
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     data = list(map(int, input().split()))
#     ans = 0
#     ans = max(data)-min(data) #최대 최소 차
# 
#     print("#{} {}".format(tc + 1, ans))