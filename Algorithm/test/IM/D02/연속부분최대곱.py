import sys
sys.stdin = open("연속부분최대곱.txt")
# N = int(input())
# ans = 1
# max_num = 0
# j = 0
# list_num = []
# for i in range(N):
#     list_num += [float(input())]
#
# for i in range(1, N):
#     ans = ans*list_num[i]
#     if ans < 1:
#         ans = 1
#
#     if max_num < ans:
#         max_num = ans
#         ans = 1
#
#     else:
#         ans = 1
# print(round(max_num, 4))


N = int(input())
ans = 1
max_num = 0
j = 1
list_num = []
for i in range(N):
    list_num += [float(input())]
if max(list_num) >= 1:
    for i in range(N):
        ans = ans*list_num[i]
        if ans < 1:
            ans = 1


        if max_num < ans:
            max_num = ans
else:
    for i in range(N):
        if max_num < list_num[i]:
            max_num = list_num[i]


print('%.3f' % max_num)

#
# #2중루프로 구현
# for i in range(N):
#     mul = 1.0
#     for j in range(i,N):
#         mul *= arr[j]
#         if mul > max:
#             max=mul
# print(max)