import sys
sys.stdin = open("이진탐색.txt")

def inorder(node):
    global i, N
    if node <= N:
        inorder(node*2)
        i += 1
        addr[node] = i
        inorder(node*2+1)


T = int(input())
for tc in range(T):
    N = int(input())
    firstChild = [0] * (N + 1)
    secondChild = [0] * (N + 1)
    addr = [0 for i in range(N+1)]
    i = 0
    inorder(1)
    print("#{} {} {}".format(tc+1, addr[1], addr[N//2]))


