import sys
sys.stdin = open("빙고.txt")

def bingo():
    CrossRDsum = 0
    CrossLDsum = 0
    cnt = 0
    for i in range(5):
        Rsum = 0
        Csum = 0
        for j in range(5):
            Rsum += arr[i][j]
            Csum += arr[j][i]
        CrossRDsum += arr[i][i]
        CrossLDsum += arr[4-i][i]
        if Rsum == 0:
            cnt += 1
        if Csum == 0:
            cnt += 1
    if CrossRDsum == 0:
        cnt += 1
    if CrossLDsum == 0:
        cnt += 1
    if cnt >= 3:
        return True
    else:
        return False


def find(num):
    global arr
    for i in range(5):
        for j in range(5):
            if num == arr[i][j]:
                arr[i][j] = 0

#빙고배열
arr = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    arr[i]=list(map(int, input().split()))

#사회자 배열
call = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    call[i]=list(map(int, input().split()))

flag = 0
for i in range(5):
    for j in range(5):
        find(call[i][j]) # 해당 숫자를 찾아 지우기
        if bingo() ==True: # 3줄의 빙고를 찾으면 탈출
            flag = 1
            break
    if flag == 1:
        break

print( i*5 + j +1) #사회자가 부른횟수
