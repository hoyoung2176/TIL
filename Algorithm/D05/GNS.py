import sys
sys.stdin = open("GNS_input.txt", "r")
T = int(input())

for tc in range(T):
    temp=input()
    data = list(map(str, input().split()))
    #숫자의 이름들
    numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    ans = []
    # counting을 해서 갯수만큼 찍어야함.
    cnt = [0]*len(numbers)
    for i in range(len(data)):
        for j in range(len(numbers)):
            #숫자의 이름과 data의 이름이 같으면 카운트한다.
            if data[i] == numbers[j]:
                cnt[j] += 1
    #카운트 한 결과물을 이용하여 숫자이름을 반복하여 답에 넣어준다.
    for x in range(len(numbers)):
        ans += [numbers[x]]*cnt[x]
    print('#{}'.format(tc+1))
    print(' '.join(ans))

    #
    # print(temp)
    # print(data)
    # print(len(data))


