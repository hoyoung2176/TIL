import sys
sys.stdin = open("글자수.txt")

T = int(input())

for tc in range(T):
    test = list(map(str, input()))
    data = list(map(str, input()))
    cnt = [0] * (len(test))
    for i in range(len(test)):
        for j in range(len(data)):
            if test[i] == data[j]:
                cnt[i] += 1

    print("#{} {}".format(tc+1,max(cnt)))

