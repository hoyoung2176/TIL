def enq(n):
    global  last
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

