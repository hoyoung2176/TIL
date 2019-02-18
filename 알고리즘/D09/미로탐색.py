dx=[0,0,-1,1]
dy=[-1,1,0,1]
x,y=(1,3)
for i in range(4):
    nx=x+dx[i]
    ny=y+dx[i]
    if check():
        data[nx][dy]=9
        dfs(nx,ny)

#사다리문제와 흡사
