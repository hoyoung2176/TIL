import sys
sys.stdin = open("회전초밥.txt")

N, d, k, c = map(int, input().split())
queue = []

for i in range(N):
    queue.append(int(input()))

max_ans = 0
for i in range(len(queue)):
    stack = []
    case = [0] * 3001
    for j in range(k):
        if (i+j) > len(queue)-1:
            if case[queue[i + j-len(queue)]] == 0:
                case[queue[(i + j) % (len(queue)-1)]] = 1
                stack += [queue[(i + j) % (len(queue)-1)]]

        else:
            if case[queue[i + j]] == 0:
                case[queue[i + j]] = 1
                stack += [queue[i+j]]

    if case[c] == 0:
        stack += [c]
    # print(stack)
    if max_ans < len(stack):
        max_ans = len(stack)
print(max_ans)

#check를 카운트로 하면 다음 체크할때 맨앞 queue 에 해당하는 숫자를 빼고 맨뒤값만 추가하면 for문 하나로 제작이 가능하다
