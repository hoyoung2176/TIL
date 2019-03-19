import sys
sys.stdin = open("암호코드 스캔.txt")

def deT(c):
    if c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10

def lenth_binary(binary_num):
    for i in range(len(binary_num) - 1, -1, -1):
        if binary_num[i] == '1':
            a = i-55
            b = i+1
            n = binary_num[a:b]
            j = a-1
            while j > 56:
                if binary_num[j] == '1':
                    b = a
                    a = b - 56
                    n = binary_num[a:b] + n
                    j -= 54
                j -= 1
            return n

sn = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
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
    temp = []
    for i in range(N):
        temp.append(input())

    #암호 16진수 추출
    flag = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] != '0':

                # 암호문으로 추측 되는 것을 16진수에서 2진수로 변환
                binary_num = ""
                for k in range(len(temp[i])):
                    binary_num += chk[deT(temp[i][k])]

                result = []
                sol = []
                # 2진수의 암호문 추출
                data = lenth_binary(binary_num)
                n = len(data) // 56
                k = len(data)
                while True:
                    result = data[k - 6] + data[k - 5] + data[k - 4] + data[k - 3] + data[k - 2] + data[k - 1] + data[k]

                    # for k in range(0, len(data), len(data)//56):

                # 암호가 정상적인지 검사
                if True:
                    flag = 1
                    break
        if flag == 1:
            break

    # print("#{} {}".format(tc + 1, len()))
