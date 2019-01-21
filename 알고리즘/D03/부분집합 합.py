arr = [-7, -3, -2, 5, 8]
n = len(arr)
sum = 0
cnt = 0
for i in range(1, 1 << n): #1<<n = 2**n
    sum = 0
    for j in range(n):
        if i & (1 << j):
            sum += arr[j]
    if sum == 0:
        cnt += 1
        for j in range(len(arr)):
            if i & (1 << j):
                print(arr[j], end = " ")
        print()
print("개수 : {}".format(cnt))
