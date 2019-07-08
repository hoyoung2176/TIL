import sys
sys.stdin = open("반나누기.txt")

def gumsa():
    # 학급 인원수 제대로 되었는지 확인
    if sum(result) < N:
        return False
    else:
        for i in range(3):
            if result[i] > Kmax or result[i] < Kmin:
                return False
        return True

T = int(input())
for tc in range(T):
    N, Kmin, Kmax = map(int, input().split())
    temp = list(map(int, input().split()))
    if N < 5 or N > 1000:
        print(-1)
        continue
    elif 3*Kmin > N or N > 3*Kmax:
        print(-1)
        continue
    else:
        temp.sort()
        nimax = max(temp)
        nimin = min(temp)
        min_ans = 1000000000000000000000
        flag = 0
        for T1 in range(nimin, nimax):
            for T2 in range(T1+1, nimax+1):
                # 인원배치
                result = [0, 0, 0]
                for i in range(N):
                    if T2 <= temp[i]:
                        result[0] += 1
                    elif T1 <= temp[i]:
                        result[1] += 1
                    elif T1 > temp[i]:
                        result[2] += 1
                if gumsa() == True:
                    if min_ans > (max(result)-min(result)):
                        flag = 1
                        min_ans = (max(result)-min(result))
        if flag == 1:
            print(min_ans)
        else:
            print(-1)


