import sys
sys.stdin = open("노드의 합.txt")

def inorder(node):
    global N
    if node <= N:
        inorder(node*2)
        addr[node] += addr[node*2]
        inorder(node*2+1)
        addr[node] += addr[node * 2+1]


T = int(input())
for tc in range(T):
    N, M, L= map(int, input().split())
    addr = [0 for _ in range((N+1)*N)]
    for i in range(M):
        temp = list(map(int, input().split()))
        addr[temp[0]] = temp[1]
    inorder(1)
    print("#{} {}".format(tc+1,addr[L]))