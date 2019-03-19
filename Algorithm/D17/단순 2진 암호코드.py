import sys
sys.stdin = open("단순 2진 암호코드.txt", "r")

sn = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    temp = []
    chk= []
    ans = []
    for i in range(N):
        temp.append(input())

    for i in range(N):
        if int(temp[i]) >= 1:
            chk = temp[i]
    i = M-1
    while i > 7:
        if chk[i] == '1':
            result = str(chk[i - 6]) + str(chk[i - 5]) + str(chk[i - 4]) + str(chk[i - 3]) + str(chk[i - 2]) + str(chk[i - 1]) + str(chk[i])
            for j in range(len(sn)):
                if result == sn[j]:
                    ans += [j]
                    i -= 6
                    break
        i -= 1

    cht1 = 0
    cht2 = 0
    cht3 = 0
    for i in range(1, len(ans)):
        cht3 += ans[i]
        if i % 2:
            cht1 += ans[i]
        else:
            cht2 += ans[i]

    if (cht1*3+cht2+ans[0]) % 10 == 0:
        print("#{} {}".format(tc+1, cht3+ans[0]))
    else:
        print("#{} {}".format(tc+1,0))