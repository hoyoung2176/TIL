import sys
sys.stdin = open("special.txt")
T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    result = [0]*10
    cnt_1 = 0
    cnt_2 = len(arr)-1
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                i=j
                arr[i], arr[min] = arr[min], arr[i]

    for x in range(10):
        if x % 2:
            result[x]=arr[cnt_1]
            cnt_1 += 1
        else:
            result[x]=arr[cnt_2]
            cnt_2 -= 1


    print("#{}".format(tc + 1), end = " ")
    for i in range(10):
        print(result[i], end =" ")
    print()