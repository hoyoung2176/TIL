def deT(c):
    if c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10

def makeT(n):
    for i in range(4):
        t.append(asc[n][i])

asc = [[0, 0, 0, 0], #0
       [0, 0, 0, 1], # 1
       [0, 0, 1, 0], # 2
       [0, 0, 1, 1], # 3
       [0, 1, 0, 0], # 4
       [0, 1, 0, 1], #5
       [0, 1, 1, 0], # 6
       [0, 1, 1, 1], # 7
       [1, 0, 0, 0], # 8
       [1, 0, 0, 1], # 9
       [1, 0, 1, 0], # 10
       [1, 0, 1, 1], # 11
       [1, 1, 0, 0], # 12
       [1, 1, 0, 1], # 13
       [1, 1, 1, 0], # 14
       [1, 1, 1, 1]  # 15
       ]

sn = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111']
temp = '0269FAC9A0'
t = []
result = []
ans = []
for i in range(len(temp)):
    makeT(deT(temp[i]))
i = len(t)-1
while i > 5:
    if t[i] == 1:
        result = str(t[i-5])+str(t[i-4]) + str(t[i-3]) + str(t[i-2]) + str(t[i-1])+ str(t[i])
        for j in range(len(sn)):
            if result == sn[j]:
                ans += [j]
                i -= 4
                break
    i -= 1

for i in range(len(ans)-1,-1,-1):
    print(ans[i], end=' ')