#숫자카드
import sys
sys.stdin = open("number_card.txt")
T = int(input())
for tc in range(T):
    N = int(input())
    data = int(input())
    ans = 0
    test_num = [0] * 10 #0~9까지 숫자를 넣을수 있는 10개의 리스트 제작
    max_count = 0
    for i in range(N):
        test_num[data % 10] +=1 #data의 값을 10으로 나누었을때 나머지 = data 값의 1의자리 숫자 해당 리스트에 넣음
        data //= 10 #data를 10으로 나눈 몫을 반환 = 1의 자리 숫자 제거
    # for i in range(N):
    #     C=[int(data[i])] += 1
    for j in range(1, 10): #0~9까지
        if test_num[j] >= max_count:
            max_count = test_num[j]
            ans = j


    print("#{} {} {}".format(tc + 1, ans, max_count))