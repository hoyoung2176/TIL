import sys
sys.stdin = open("이진수2.txt")
T = int(input())

for tc in range(T):
    temp=float(input())
    i = 0
    data = ""
    # while i <= 12:
    while True:
        i += 1
        temp *= 2
        data += str(temp)[0]
        temp -= int(str(temp)[0])

        if temp == 0.0:
            print('#{} {}'.format(tc + 1, data))
            break
        if len(data) >= 13:
            print('#{} overflow'.format(tc + 1))
            break
