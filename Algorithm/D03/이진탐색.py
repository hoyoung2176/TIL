#제약조건 : 정렬이 되어 있어야한다.
def binarySearch(a, key):
    start = 0
    end = len(a) -1
    while start <= end:
        middle = (end + start) // 2
        if key == a[middle]: #검색성공
            return middle
        elif key < a[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1 #검색실패

key = 22
data = [2, 4, 7, 9, 11, 19, 23]
print(binarySearch(data,key))