import sys
sys.stdin = open("문자열 비교.txt")

T = int(input())

for tc in range(T):
    test = list(map(str,input()))
    data = list(map(str,input()))
    for i in range(len(data)-len(test)+1):
        a = []
        for j in range(len(test)):
            a.append(data[i])
            i += 1
        if a == test:
            ans = 1
            break
        else:
            ans = 0
    print("#{} {}".format(tc+1, ans))
