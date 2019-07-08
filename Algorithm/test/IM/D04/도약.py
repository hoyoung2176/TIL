import sys
sys.stdin = open("도약.txt")

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

arr.sort()
ans = 0
for i in range(N-2):
    first_locate = arr[i]
    for j in range(i+1, N-1):
        second_locate = arr[j]
        jump1 = second_locate - first_locate
        for k in range(j+1, N):
            Third_locate = arr[k]
            jump2 = Third_locate- second_locate
            if jump2 <= 2*jump1 and jump2>=jump1:
                ans += 1
            if jump2 > 2*jump2: #이전 뛴거리 두배이상이면 탈출
                break

print(ans)