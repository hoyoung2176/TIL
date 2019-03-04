import sys
sys.stdin = open('덧셈.txt')

S, ans = map(str, input().split())
flag = 0
result = 0
while flag < len(S)-1:
    SA = str()
    SB = str()
    flag += 1
    for i in range(flag):
        SA += S[i]
    for j in range(flag, len(S)):
        SB += S[j]
    if int(SA) + int(SB) == int(ans):
        result = 1
        print('{}+{}={}'.format(int(SA), int(SB), int(ans)))


if result == 0:
    print('NONE')
