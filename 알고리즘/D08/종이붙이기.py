#재귀
import sys
import math
# sys.stdin = open("종이붙이기.txt")
sys.stdin = open("test.txt")
T = int(input())

def paper(N, r):
   if N > r:
       ans = math.factorial(N) / (math.factorial(r)*math.factorial(N-r))



for tc in range(T):
    N = int(input()) // 10
    cnt = 0
    r = 0
    result = 0
    cnt_1 = 0
    while N > r:
        if r > 0:
            result += paper(N, r) * 2 * r
        else:
            result += paper(N, r)
        N -= 1
        r += 1
    r -= 1
    cnt = result
    print(cnt)



