import sys
sys.stdin = open('월동준비.txt')
N = int(input())
food = list(map(int, input().split()))
max_food = -1000000000
cnt_1 = 0
cnt = 0
# 최대합 문제

#멍청한 다람쥐
for i in range(N):
    cnt_1 += food[i]

    if max_food < cnt_1:
        max_food = cnt_1
    if cnt_1 < 0:
        cnt_1 = 0





# j = 0
# while j < N:
#     j += 1
#     for i in range(1,N-j+1):
#         for k in range(j):
#             cnt_1 += food[i+k-1]
#
#         if max_food < cnt_1:
#             max_food = cnt_1
#             cnt_1 = 0
#
#         else:
#             cnt_1 = 0


#똑똑한 다람쥐
cnt_2 = 0
food_1 = -1000000000000
max_food_2 = 0

for i in range(N):
    if food[i] > 0:
        max_food_2 += food[i]
        cnt_2 += 1
    else:
        if food_1 <food[i]:
            food_1 = food[i]
if cnt_2 == 0:
    max_food_2 = food_1

print("{} {}".format(max_food, max_food_2))
