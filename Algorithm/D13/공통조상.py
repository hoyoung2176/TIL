def find(node):
    global newlist
    if node != 0:
        newlist.append(tree[node][2])
        find(tree[node][2])

def order(node):
    global cnt
    if node != 0:
        order(tree[node][0])
        order(tree[node][1])
        cnt += 1
        # print(node, end = " ")


import sys
sys.stdin = open('공통조상.txt')



T = int(input())
for tc in range(T):
    V, E, num1, num2 = map(int, input().split())
    temp = list(map(int, input().split()))
    tree = [[0 for _ in range(3)] for _ in range(V+1)]

    for i in range(E):
        n1 = temp[i * 2]
        n2 = temp[i * 2 + 1]
        if not tree[n1][0]:
            tree[n1][0] = n2
        else:
            tree[n1][1] = n2

        tree[n2][2]  = n1

    newlist = []
    find(num1)
    num1list = newlist
    newlist = []
    find(num2)
    num2list = newlist
    flag = 0
    cnt = 0
    print('#{}'.format(tc+1), end = " ")
    for i in range(len(num1list)):
        for j in range(len(num2list)):
            if num1list[i] == num2list[j]:
                flag = 1
                order(num1list[i])

                print("{} {}".format(num1list[i], cnt))
                break
        if flag == 1:
            break
