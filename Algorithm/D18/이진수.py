import sys
sys.stdin = open("이진수.txt")

def deT(c):
    if c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10



T = int(input())
chk = ['0000',
       '0001',
       '0010',
       '0011',
       '0100',
       '0101',
       '0110',
       '0111',
       '1000',
       '1001',
       '1010',
       '1011',
       '1100',
       '1101',
       '1110',
       '1111'
       ]

for tc in range(T):
    N, temp = map(str,input().split())
    binary_list = ""


    for i in range(len(temp)):
        binary_list += chk[deT(temp[i])]

    print("#{} {}".format(tc+1,binary_list))