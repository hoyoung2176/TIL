import sys
sys.stdin = open("숫자근.txt")

# T = int(input())
# max_num = 0
# dr = 0
# for tc in range(T):
#     num = int(input())
#     result = []
#     ans = num
#     max_num = 0
#
#
#     while ans > 0:
#         result.append(ans % 10)
#         ans = ans // 10
#
#
#     while len(result) > 0:
#         ans += result.pop()
#
#         if len(result) == 0 and ans >= 10:
#
#             while ans > 0:
#                 result.append(ans % 10)
#                 ans = ans // 10
#
#
#     if max_num < ans:
#         max_num = ans
#         dr = num
#
# print(dr)

N=int(input())
arr=[]
for i in range(N):
    arr.append(int(input()))


def root_calc(num): #숫자근 만들어주는 함수

    while True:
        temp = list(map(int,str(num)))
        tot = sum(temp)
        if tot<10 : return tot
        num=tot
    '''
    while True:
        tot = 0
        while num > 0:
            tot += num % 10
            num = num // 10

        if ans < 10:
            return tot
        num = tot
    '''

root_max = 0
sol = 0
for i in range(N):
    root = root_calc(arr[i])
    #가장 큰 숫자근이면 해당 정수를 솔루션으로
    if root_max<root:
        root_max = root
        sol = arr[i]

    #가장 큰 숫자근과 같다면 더 작은 정수를 솔루션으로

    if root_max == root:
        if sol > arr[i]:
            sol = arr[i]
print(sol)





