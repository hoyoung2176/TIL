def result(node):
    global ans, num_list
    if num_list[node] == '-':
        ans = num_list[firstChild[node]] - num_list[secondChild[node]]
        num_list[node] = ans
    elif num_list[node] == '+':
        ans = num_list[firstChild[node]] + num_list[secondChild[node]]
        num_list[node] = ans
    elif num_list[node] == '*':
        ans = num_list[firstChild[node]] * num_list[secondChild[node]]
        num_list[node] = ans
    elif num_list[node] == '/':
        if num_list[firstChild[node]] != 0 and num_list[secondChild[node]] != 0:
            ans = num_list[firstChild[node]] // num_list[secondChild[node]]
            num_list[node] = ans
        else:
            return

def inorder(node):
    global ans
    if node != 0:
        inorder(firstChild[node])
        inorder(secondChild[node])
        result(node)



import sys
sys.stdin = open('사칙연산.txt')

T = 10
for tc in range(T):
    ans = 0
    N = int(input())
    firstChild = [0] * (N+1)
    secondChild = [0] * (N+1)
    num_list = [0]*(N+1)
    # ch = [0] * (N + 1)
    for i in range(N):
        temp = list(input().split())
        addr = int(temp[0])
        if len(temp) == 2:
            num = int(temp[1])
            num_list[addr] = num
        else:
            # ch[addr] = temp[1]
            num_list[addr] = temp[1]
            if addr * 2 <= N:
                firstChild[addr] = int(temp[2])
                if addr * 2 + 1 <= N:
                    secondChild[addr] = int(temp[3])

    print('#{}'.format(tc+1), end= " ")
    inorder(1)
    print(ans)



