def Counting_Sort(A, B, C):
    #A [1 .. n] -- 입력배열 (1 to k)
    #B [1 .. n] -- 정렬된 배열.
    #C [1 .. k] -- 카운트배열

    for i in range(1, len(A)):
        C[A[i]] +=1

    for i in range(1, len(C)):
        C[i] += C[i-1]

    for i in range(len(B)-1, -1, -1): #거꾸로 마지막부터 0까지 -1씩감소
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= -1

A = [1, 4, 5, 1, 2, 4, 5, 7, 9, 3]
B = [0] * len(A)
C = [0] * 10 #k를 10으로 가정, C =[0]*k
Counting_Sort(A, B, C)
print(B)