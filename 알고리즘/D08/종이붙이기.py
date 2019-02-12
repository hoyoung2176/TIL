#재귀
import sys
sys.stdin = open("종이붙이기.txt")

T = int(input())

def paper(N):
    if N == 0:
        return 1
    elif N < 2:
        return N
    else:
        return paper(N - 1) + 2*paper(N - 2)

for tc in range(T):
    N = int(input())//10
    print("#{} {}".format(tc+1, paper(N)))