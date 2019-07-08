N = int(input())
temp = list(map(int, input().split()))
arr = []
for i in range(N):
    SL = temp[2*i]
    SW = temp[2*i+1]
    arr.append((SL, SW),)

arr.sort(key=lambda x: x[0])
chk = [0]* N
# print(arr)

cnt = 0
for i in range(N):
    if not chk[i]:              # 처음 값 넣기
        cnt += 1
        chk[i] = 1
        W = arr[i][1]
    for j in range(i+1, N):     # 초기값과 비교하여 작으면 패스, 크거나 같으면 체크하고 초기값변경
        if W > arr[j][1]:
            continue
        if not chk[j]:
            chk[j] = 1
            W = arr[j][1]
print(cnt)
