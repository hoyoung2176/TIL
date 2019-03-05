import sys
sys.stdin = open("subtree.txt")

def find(node):
    global cnt
    if node != 0:
        find(tree[node][0])
        find(tree[node][1])
        cnt += 1


T = int(input())
for tc in range(T):
    cnt = 0
    E, N = map(int, input().split())
    temp = list(map(int, input().split()))
    tree = [[0 for _ in range(3)] for _ in range(E+2)]
    for i in range(E):
        n1 = temp[i*2]
        n2 = temp[i*2 +1]
        if not tree[n1][0]:
            tree[n1][0] = n2
        else:
            tree[n1][1] = n2
        tree[n2][2] = n1
    find(N)
    print("#{} {}".format(tc+1, cnt))