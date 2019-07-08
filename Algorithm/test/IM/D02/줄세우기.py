import sys
sys.stdin = open('줄세우기.txt')

N = int(input())
num = list(map(int,input().split()))
arr = [i+1 for i in range(len(num+1))]
K = 0
for i in range(1, len(num)):

print(ans)