import sys
sys.stdin = open("Flatten.txt")
T = 10
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    ans = 0
    max_num = data[0]
    min_num = data[0]

    for j in range(N):
        max_num = data[0]
        min_num = data[0]
        for i in range(len(data)): #data에 있는 것을 i에 넣어 판단.
            if data[i] >= max_num: #max와 min을 i와 비교하여 스왑합니다.
                max_num = data[i]
                max_index = i

            if data[i] <= min_num:
                min_num = data[i]
                min_index = i

        data[max_index] -= 1
        data[min_index] += 1



    max_num0 = data[0]
    min_num0 = data[0]


    for n in range(len(data)): #data에 있는 것을 i에 넣어 판단.

        if data[n] > max_num0: #max와 min을 i와 비교하여 스왑합니다.
            max_num0 = data[n]
        if data[n] <= min_num0:
            min_num0 = data[n]
    ans = max_num0 - min_num0


    # ans = max(data) - min(data)
    print("#{} {}".format(tc + 1, ans))
