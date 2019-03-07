import sys
sys.stdin = open("초콜릿공장.txt")
N = int(input())
cnt = 0
for _ in range(N):
    temp = list(input().split())
    L = list(temp[0])
    H = list(temp[1])

    #불량이 있으면 1 없으면 0
    flag = 0

    #두회사간 중복검사
    cnt_2 = 0

    # L사 내부의 불량 검사
    for i in range(len(L)-1):
        for j in range(i+1, len(L)):
            if L[i] == L[j]:
                flag = 1
                break
        if flag == 1:
            break

    # H사 내부의 불량 검사
    for i in range(len(H)-1):
        for j in range(i+1, len(H)):
            if H[i] == H[j]:
                flag = 1
                break
        if flag == 1:
            break

    #L사와 H사 비교
    for i in range(len(L)):
        for j in range(len(H)):
            if L[i] == H[j]:
                cnt_2 += 1
                if cnt_2 >= 2:
                    flag = 1
                    break
        if flag == 1:
            break
    if flag == 1:
        cnt += 1

print(cnt)