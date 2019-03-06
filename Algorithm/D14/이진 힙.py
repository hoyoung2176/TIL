import sys
sys.stdin = open("이진 힙.txt")


def enq(n):
    global last
    last += 1 #마지막 노드 번호증가
    c = last # 마지막 노드를 자식 노트로
    p = c//2 #부모 노드 번호 계산
    q[last] = n #마지막 노드에 값 저장
    while c > 1 and q[p] > q[c]: #루트가 아니고, 부모의 노드보다 자식의 노드값이 클때
        t = q[p]    #저장값 바꿈
        q[p] = q[c]
        q[c] = t
        c = p   #부모를 새로운 노드로
        p = p // 2

T = int(input()) #테스트케이스 받음
for tc in range(1,T+1):
    N = int(input()) #노드의 갯수
    data = list(map(int, input().split()))  #데이터 받기

    last = 0  #마지막 노드의 번호
    q = [0 for _ in range(len(data)+1)]  #트리

    for i in range(len(data)): #트리에 데이터 넣기
        enq(data[i])

    ans = 0
    node = len(q)-1

    while node > 0:
        ans +=q[node//2]
        node = node // 2
    print('#{} {}'.format(tc, ans))