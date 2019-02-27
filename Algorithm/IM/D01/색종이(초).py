import sys
sys.stdin = open("색종이.txt")


N = int(input())
data = [[0 for _ in range(100)] for _ in range(100)]

for tc in range(N):
    R, C = map(int, input().split())
    for i in range(R, R+10):
        for j in range(C, C+10):
            data[i][j] = 1

#도화지에 면적구하기
cnt = 0
for i in range(100):
    for j in range(100):
        cnt += data[i][j]


# print(data)
print(cnt)