#삼성 SW 전기버스
import sys
sys.stdin = open("busstop.txt")
T = int(input())
for tc in range(T):
    K, N, M = map(int, input().split()) #K는 버스가 충전시 이동가능 거리, N 는 최대 거리, M은 충전소 수
    data = list(map(int, input().split())) #data는 충전소의 위치
    ans = 0
    m=K #버스가 이동한 거리

    while m < N:
        if m not in data: #버스가 이동한 곳이 충전소가 아닐경우
            m -= 1
            c +=1
            if c == K: #c는 버스 이동 카운트. K안에 충전소가 있는지에 대한 판단근거
                ans = 0 #K안에 충전소가 있는지에 대한 판단근거
                break
        if m in data: #이동한 곳이 충전소일시
            ans += 1 #충전소 들린 횟수
            c=0 #충전소 판단 카운트 초기화
            m += K #K만큼 이동시킴

    print("#{} {}".format(tc + 1, ans))