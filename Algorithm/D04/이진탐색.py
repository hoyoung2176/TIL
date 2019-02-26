import sys
sys.stdin = open("book.txt")
T = int(input())
for tc in range(T):
    P, Pa, Pb = list(map(int, input().split()))
    cnt_A = 0
    cnt_B = 0
    start = 1
    end = P
    while start <= end:
        c = int((start + end) // 2)
        if c == Pa:
            start = 1
            end = P
            cnt_A += 1
            break
        elif Pa < c:
            end = c
            cnt_A += 1
        else:
            start = c
            cnt_A += 1

    while start <= end:
        c = int((start + end) // 2)
        if c == Pb:
            start = 1
            end = P
            cnt_B += 1
            break
        elif Pb < c:
            end = c
            cnt_B += 1
        else:
            start = c
            cnt_B += 1


    if cnt_B == cnt_A:
        print("#{} {}".format(tc + 1, 0))
    elif cnt_B > cnt_A:
        print("#{} {}".format(tc + 1, "A"))
    else:
        print("#{} {}".format(tc + 1, "B"))