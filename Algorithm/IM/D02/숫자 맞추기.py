import sys
sys.stdin = open('숫자맞추기.txt')
N = int(input())
arr = [[0 for _ in range(3)] for _ in range(N)]
ans = [0 for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))

for i in range(3):
    flag = 0
    for j in range(N-1):
        for k in range(j+1, N):
            if arr[j][i] == arr[j][i]:
                flag = 1
                break
            else:
                ans[i] = arr[j][i]
        # if flag == 1:
        #     break

print(ans)