import sys
sys.stdin = open('피자 굽기.txt')

T = int(input())
for tc in range(T):
    # N은 오븐에 최대로 들어갈 수 있는 갯수, M은 피자의 갯수
    N, M = map(int, input().split())

    # 치즈의 인덱스와 값을 튜플형식으로 저장한다.
    data = list(map(int, input().split()))
    data = list(enumerate(data))


    oven = []
    queue = []

    #N개의 피자를 순서대로 일단 화덕에 넣기
    for i in range(N):
        oven.append(data.pop(0))

    #오븐에 하나가 남을때까지 루프
    while len(oven) > 1:
        #오븐에서 치즈 상태 확인하여 다 녹지 않았으면 회전
        if oven[0][1]//2 != 0:
            queue = list(oven.pop(0))
            oven.append((queue[0],queue[1]//2))

        #다 녹았으면 빼내기
        else:
            oven.pop(0)
            # 아직 안 구운 피자가 있으면 오븐에 추가
            if data:
                oven.append(data.pop(0))

    #오븐에 남은 하나의 인덱스값을 추출한다. 처음시작이 1이므로 +1하였다.
    print("#{} {}".format(tc+1 ,oven[0][0]+1))