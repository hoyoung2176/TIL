import sys
sys.stdin = open('덧셈.txt')
#
# S, ans = map(str, input().split())
# flag = 0
# result = 0
# while flag < len(S)-1:
#     SA = str()
#     SB = str()
#     flag += 1
#     for i in range(flag):
#         SA += S[i]
#     for j in range(flag, len(S)):
#         SB += S[j]
#     if int(SA) + int(SB) == int(ans):
#         result = 1
#         print('{}+{}={}'.format(int(SA), int(SB), int(ans)))
#
#
# if result == 0:
#     print('NONE')


# 슬라이스를 이용한 풀이
# num, ans = map(int, input().split())
# arr = str(num)
# N = len(arr)
#
# #정수 두개로 분리
# for i in range(N-1):
#     a = int(arr[:i+1])
#     b = int(arr[i+1:])
#     print(a,b)

#정수 3개로 분리
for i in range(N-2):
    A = int(arr[:i+1])
    for j in range(i+1, N-1):
        B = int(arr[i+1:j+1])
        C = int(arr[j+1:])
        print(A, B, C)

