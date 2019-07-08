import sys
sys.stdin=open('수열.txt')

N = input().split()
temp = list(map(int, input().split()))
stack = a = temp.pop(0)
flag = 0
result = 0
cnt = 0
sol = 0
while len(temp) != 0:
    a = temp.pop(0)

    if len(temp) != 0:
        #이전값보다 증가할때
        if stack[-1] == a:
            stack += [a]
            cnt += 1
        elif stack[-1] - a > 0:
            if flag == 0 or flag == 1:
                flag = 1
                stack += [a]
                cnt += 1

            else:
                flag = 1
                cnt = 0
                stack = []
                stack += [a]
                cnt += 1
        elif stack[-1] - a < 0:
            if flag == 0 or flag == 2:
                flag = 1
                cnt += 1
                stack += [a]
            else:
                flag = 2
                cnt = 0
                stack = []
                stack += [a]
                cnt += 1


    elif len(temp) == 0:
        stack += [a]
        cnt += 1

    if sol < cnt:
        sol = cnt
        print(stack)

print(sol)