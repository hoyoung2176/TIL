import sys
sys.stdin = open("연속부분최대곱.txt")
N = int(input())
ans = 1
max_num = 0
j = 0
list_num = []
for i in range(N):
    list_num += [float(input())]

while j < N:
    j += 1
    for i in range(1, N-j+1):
        for k in range(j):
            ans = ans*list_num[i+k-1]

        if max_num < ans:
            max_num = ans
            ans = 1

        else:
            ans = 1
print(round(max_num,4))