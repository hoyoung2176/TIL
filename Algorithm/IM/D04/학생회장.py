import sys
sys.stdin = open('학생회장.txt')
#
# #회장선거
# def battle():
#     # 1번이 회장인경우
#     if ans1 > ans2 and ans1 > ans3:
#         return 1, ans1
#
#     # 2번이 회장인 경우
#     elif ans2 > ans1 and ans2 > ans3:
#         return 2, ans2
#
#     #3번이 회장인경우
#     elif ans3 > ans2 and ans3 > ans1 :
#         return 3, ans3
#
#     # 동점자 발생의경우
#     # 1번, 3번이 가장 클 경우
#     elif ans1 > ans2 and ans1 == ans3:
#         if result1[3] > result3[3]:
#             return 1, ans1
#         elif result1[3] < result3[3]:
#             return 3, ans3
#         elif result1[3] == result3[3]:
#             if result1[2] > result3[2]:
#                 return 1, ans1
#             elif result1[2] < result3[2]:
#                 return 3, ans3
#             else:
#                 return 0, ans1
#
#     #1번, 2번이 가장 큰 경우
#     elif ans1 > ans3 and ans1 == ans2:
#         if result1[3] > result2[3]:
#             return 1, ans1
#         elif result1[3] < result2[3]:
#             return 2, ans2
#         elif result1[3] == result2[3]:
#             if result1[2] > result2[2]:
#                 return 1, ans1
#             elif result1[2] < result2[2]:
#                 return 2, ans2
#             else:
#                 return 0, ans1
#
#     # 2번, 3번이 가장 큰 경우
#     elif ans2 > ans1 and ans2 == ans3:
#         if result2[3] > result3[3]:
#             return 2, ans2
#         elif result2[3] < result3[3]:
#             return 3, ans3
#         elif result2[3] == result3[3]:
#             if result2[2] > result3[2]:
#                 return 2, ans2
#             elif result2[2] < result3[2]:
#                 return 3, ans3
#             else:
#                 return 0, ans2
#     #3명다 동점자인 경우
#     elif ans1 == ans2 == ans3:
#         # 3점짜리가 1이 가장 큰경우
#         if result1[3] > max(result2[3], result3[3]):
#             return 1, ans1
#         elif result2[3] > max(result1[3], result3[3]):
#             return 2, ans2
#         elif result3[3] > max(result1[3], result2[3]):
#             return 3, ans3
#         # 3점짜리가 1,2 가 같은경우
#         if result1[3] > result3[3] and result1[3] == result2[3]:
#             if result1[2] > result2[2]:
#                 return 1, ans1
#             elif result1[2] < result2[2]:
#                 return 2, ans2
#             else:
#                 return 0, ans1
#         # 3점짜리가 1,3 가 같은경우
#         elif result1[3] > result2[3] and result1[3] == result3[3]:
#             if result1[2] > result3[2]:
#                 return 1, ans1
#             elif result1[2] < result3[2]:
#                 return 3, ans3
#             else:
#                 return 0, ans1
#         # 3점짜리가 2,3 이 같은경우
#         elif result2[3] > result1[3] and result2[3] == result3[3]:
#             if result2[2] > result3[2]:
#                 return 2, ans2
#             elif result2[2] < result3[2]:
#                 return 3, ans3
#             else:
#                 return 0, ans2
#         else:
#             return 0, ans1
#
#     else:
#         return 0, max(ans1, ans2, ans3)
#
# def gumsa(arr):
#     gumsa_list = [0, 0, 0]
#     for i in range(len(arr)):
#         gumsa_list[arr[i]-1] += 1
#     if min(gumsa_list) == 1:
#         return True
#     else:
#         return False
#
#
#
N = int(input())
# arr = [0, 0, 0]
# result1 = [0, 0, 0, 0]
# result2 = [0, 0, 0, 0]
# result3 = [0, 0, 0, 0]
# ans1 = 0
# ans2 = 0
# ans3 = 0
#
# for i in range(N):
#     arr = list(map(int, input().split()))
#     #무효표 검사
#     if gumsa(arr) == True:
#         result1[arr[0]] += 1
#         result2[arr[1]] += 1
#         result3[arr[2]] += 1
#
#         ans1 += arr[0]
#         ans2 += arr[1]
#         ans3 += arr[2]
#
#
# print(*battle())

arr = [[0]*5 for _ in range(4)] # 행을 후보자 열을 1,2,3 점수대로 4열은 합계
for i in range(N):
    score = list(map(int, input().split()))
    for j in range(1,4): #후보자 3명
        arr[j][score[j-1]]+=1 #후보자별 점수별 카운트

for i in range(1,4): #후보자별 합계
    for j in range(1,4):
        arr[i][4] += arr[i][j]*j


for i in range(1,4):
    for j in range(1,5):
        print(arr[i][j], end = " ")
    print()