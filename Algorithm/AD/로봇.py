def BFS(r, c, ndir):
    # 정보 테이블, 인덱스 0: 동, 1: 서, 2:남, 3:북
    dr = (0, 0, 0, 1, -1)
    dc = (0, 1, -1, 0, 0)
    turn = [(0, 0), (4, 3), (3, 4), (1, 2), (2, 1)]

    queue = []
    # 1] 시작점을 큐에 저장(방문표시)
    queue.append((r, c, ndir),)
    while queue:

        # 2] 큐에서 데이터 읽기
        for i in range(1, 4):   # go 1, 2, 3, i는 증감치

        for i in range(2):      # Turn lift, right


# main--------------------------------------
R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
chk = [[[0]*C for i in range(R)] for j in range(5)]     # 3차원 배열// [면][행][열]
sr, sc, sdir = map(int, input().split())
er, ec, edir = map(int, input().split())
sol=BFS()
print(sol)