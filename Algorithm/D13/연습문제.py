def preorder(node):
    if node != 0:
        print("{}".format(node), end=" ")
        preorder(tree[node][0])
        preorder(tree[node][1])


def inorder(node):
    if node != 0:
        inorder(tree[node][0])
        print("{}".format(node), end=" ")
        inorder(tree[node][1])


def postorder(node):
    if node != 0:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print("{}".format(node), end=" ")

def printTree():
    for i in range(1, V+1):
        print("%2d %2d %2d" % (i, tree[i][0], tree[i][1]))


import sys
sys.stdin = open('연습문제.txt')

N = int(input())
tree = [[0 for _ in range(3)] for _ in range(N+1)]
data = list(map(int,input().split()))

while len(data) != 0:
    x = data.pop(0)
    y = data.pop(0)
    if tree[x][0] == 0:
        tree[x][0] = y
    else:
        tree[x][1] = y
        tree[y][2] = x

# for i in range(E):
#     n1 = temp[i*2]
#     n2 = temp[i*2+1]
#     if not tree[n1][0]:
#         tree[n1][0] = n2
#     else:
#         tree[n1][1] = n2

# printTree()

# for i in range(1, len(tree)):
#     print(i, end=" ")
#     for j in range(len(tree[0])):
#         print(tree[i][j], end=" ")
#     print()

inorder(1)