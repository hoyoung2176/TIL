import sys
sys.stdin = open("회문.txt")

T = int(input())

for tc in range(T):
    N, M = list(map(int, input().split()))

    #arr 제작
    data = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        data[i] = list(map(str, input()))

    middle = M // 2
    ans1=0
    ans2=0
    #좌우 순회
    #행 소환
    for x in range(N):
        for y in range(N-M+1):
            cnt = 0
            ans = [0]*M
            #열 반복
            if M % 2:
                for j in range(middle):
                    # 검사
                    if data[x][y + j] == data[x][M - j - 1 + y]:
                        cnt += 1
                        ans[j] = (data[x][y + j])
                        ans[M - j - 1] = (data[x][y + j])

                    else:
                        break
                if cnt == middle:
                    ans[middle] = data[x][+y + middle]
                    ans1 = ans
            else:
                for j in range(middle):
                    #검사
                    if data[x][y+j] == data[x][M-j-1+y]:
                        cnt += 1
                        ans[j] = (data[x][y+j])
                        ans[M-j-1] = (data[x][y+j])
                    else:
                        break
                if cnt == middle:
                    ans1 = ans


    for x in range(N):
        for y in range(N-M+1):
            cnt = 0
            ans = [0]*M
            #열 반복
            if M % 2:
                for j in range(middle):
                    #검사
                    if data[y+j][x] == data[M-j-1+y][x]:
                        cnt += 1
                        ans[j] = (data[y+j][x])
                        ans[M-j-1] = (data[y+j][x])

                    else:
                        break
                if cnt == middle:
                    ans[middle] = data[y + middle][x]
                    ans1 = ans
            else:
                for j in range(middle):
                    #검사
                    if data[y+j][x] == data[M-j-1+y][x]:
                        cnt += 1
                        ans[j] = (data[y+j][x])
                        ans[M-j-1] = (data[y+j][x])

                    else:
                        break
                if cnt == middle:
                    ans1 = ans
    print('#{} {}'.format(tc +1, ''.join(ans1)))


