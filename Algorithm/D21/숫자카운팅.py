N = int(input())
temp = list(map(int, input().split()))
M = int(input())
data = list(map(int, input().split()))
ans = [0 for _ in range(max(temp)+1)]
for i in range(len(temp)):
    ans[temp[i]] += 1

for i in range(len(data)):
    print(ans[data[i]], end=" ")