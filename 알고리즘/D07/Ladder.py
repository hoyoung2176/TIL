import sys
sys.stdin = open("Ladder.txt")

T=10

for tc in range(T):
    #data 받아오기
    N = input()
    SIZE = 100
    data = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    result_x = 0
    for i in range(SIZE):
        data[i] = list(map(int, input().split()))

    x = SIZE - 1
    result_x = data[x].index(2)
    #당첨위치로부터 위로 올라가면서 사다리 타기
    while x > 0:
        # 왼쪽 이동
        if result_x > 0 and data[x][result_x - 1] != 0:
            while result_x > 0 and data[x][result_x - 1] != 0:
                result_x -= 1
        # 오른쪽이동
        elif result_x < SIZE - 1 and data[x][result_x + 1] != 0:
            while result_x < SIZE - 1 and data[x][result_x+1] != 0:
                result_x += 1
        x -= 1

    print("#{} {}".format(tc+1, result_x))

# #당첨위치 찾기
# for j in range(SIZE):
#     if data[SIZE-1][j] == 2:
#         result_x = j
