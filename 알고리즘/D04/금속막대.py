import sys
sys.stdin = open("금속막대.txt")
T = int(input())
for tc in range(T):
    n = int(input())
    list_test = list(map(int, input().split()))
    nasa1 = []
    nasa2 = []
    nasa3 = [0]*n
    nasa4 = [0]*n
    # nasa = []*n
    #나누기
    for i in range(len(list_test)):
        if i % 2 == 0:
            nasa1.append(list_test[i]) #수나사
        else:
            nasa2.append(list_test[i]) #암나사

    #맨 앞 숫자 넣기
    for x in range(len(nasa1)):
        if nasa1[x] not in nasa2:
            nasa1[0], nasa1[x] = nasa1[x], nasa1[0]
            nasa2[0], nasa2[x] = nasa2[x], nasa2[0]

    for j in range(1,len(nasa1)):
        if nasa1[j] == nasa2[j-1]:
            nasa1[j] = nasa1[j]
            nasa2[j] = nasa2[j]
        else:
            for y in range(len(nasa1)):
                if nasa1[y] == nasa2[j-1]:
                    nasa1[j], nasa1[y] = nasa1[y], nasa1[j]
                    nasa2[j], nasa2[y] = nasa2[y], nasa2[j]


    print("#{}".format(tc + 1), end = " ")
    for i in range(len(nasa1)):
        print(nasa1[i], end =" ")
        print(nasa2[i], end=" ")
    print()

