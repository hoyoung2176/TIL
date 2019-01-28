#고지식한 패턴 검색 알고리즘
def Brute_Force(text,pattern):
    i, j = start, 0

    while i < len(text) and j < len(pattern):
        if text[i] != pattern[j]:
            i = i - j
            j = -1
        i = i+1
        j = j+1

    if j == len(pattern):
        return i - len(pattern)
    else:
        return i

def Brute_Force2(text, pattern):
    for i,j in range(len(text) - range(len(pattern)+1)):
        cnt = 0
        for j in range(len(pettern)):
            if text[i+j] != pattern[j]:
                break
            else:
                cnt+=1



text = "This is a book. This is a computer"
pattern = "is"
print(Brute_Force(text, pattern))

start = 0
while True:
    start =Brute_Force(text,pattern)
    if start >

