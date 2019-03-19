import sys
sys.stdin = open("암호코드 스캔.txt")

def deT(c):
    if c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10

def gumsa(c, b, a):
    for i in range(len(sn)):
        if sn[i] == (c, b, a):
            return i

sn = [(2, 1, 1), (2,2,1), (1,2,2), (4,1,1), (1,3,2), (2,3,1), (1,1,4), (3,1,2), (2,1,3), (1,1,2)]
chk = ['0000', # 0
       '0001', # 1
       '0010', # 2
       '0011', # 3
       '0100', # 4
       '0101', # 5
       '0110', # 6
       '0111', # 7
       '1000', # 8
       '1001', # 9
       '1010', # A
       '1011', # B
       '1100', # C
       '1101', # D
       '1110', # E
       '1111'  # F
       ]

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    #2진법 저장
    arr = []
    for i in range(N):
        temp = input()
        data = ""
        for j in range(M):
            data += chk[deT(temp[j])]
        arr.append(data)

    for i in range(N):
        if int(arr[i]) != 0:
            for j in range(len(arr)-1, -1, -1):
                result = []
                #암호 시작점찾기
                if arr[i][j] == '1' and arr[i-1][j] == '0' and arr[i][j+1] == '0':
                    flag = '1'
                    k = j
                    a, b, c = 0, 0, 0
                    cnt = 0
                    while k != 0:
                        if arr[i][k] == flag:
                            if cnt == 0:
                                a += 0
                            elif cnt == 1:
                                b += 1
                            elif cnt == 2:
                                c += 1
                        else:
                            cnt += 1
                            flag = arr[i][k]
                            if cnt > 2:
                                cnt = 0
                                minnum = min(a, b, c)
                                #암호문의 값은 무엇인지 나타내기
                                result += [gumsa(c//minnum, b//minnum, a//minnum)]
                                a, b, c = 0, 0, 0
                            if cnt == 0:
                                a += 0
                            elif cnt == 1:
                                b += 1
                            elif cnt == 2:
                                c += 1
                        k -= 1



