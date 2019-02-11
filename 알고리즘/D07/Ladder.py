import sys
sys.stdin = open("Ladder.txt")

T=1
for tc in range(T):
#델타검색
    #data 받아오기
    no = int(input())
    SIZE = 100
    data = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    result_x = 0
    for i in range(SIZE):
        data[i] = list(map(int,input().split()))

    #당첨위치 찾기
    for j in range(SIZE):
        if data[SIZE-1][j] == 2:
            result_x = j

    x = SIZE - 2
    #당첨위치로부터 위로 올라가면서 사다리 타기
    while x > 0:
        if result_x+1 <= SIZE and result_x-1 >=0:
            #왼쪽 이동
            if data[x][result_x-1] == 1:
                result_x -= 1

                while data[x][result_x-1] == 1:
                    if result_x+1 <= SIZE and result_x-1 >= 0:
                        result_x -= 1



            #오른쪽이동
            elif data[x][result_x + 1] == 1:

                    result_x += 1

                    while data[x][result_x+1] == 1:
                        if result_x+1 <= SIZE and result_x-1 >= 0:
                            result_x += 1


            else:
                x -= 1
        else:
            break

    print("#{} {}".format(tc+1, result_x))
