import sys
sys.stdin = open("토너먼트.txt")


def gruop(dict_data):
    global result
    if len(dict_data) > 2:
        if len(dict_data) % 2:
            group_01 = dict_data[0:len(dict_data) // 2+1]
            group_02 = dict_data[len(dict_data) // 2+1: len(dict_data)]
        else:
            group_01 = dict_data[0:len(dict_data)//2]
            group_02 = dict_data[len(dict_data)// 2 : len(dict_data)]
        gruop(group_01)
        gruop(group_02)
    else:
        gumsa(dict_data)

    if len(result) >= 2:
        data_01 = result
        result = []
        gruop(data_01)
    else:
        return result


def partition(a, l, r):
    pivot = a[l]
    i = l
    j = r

    while i < j:
        while a[i] <= pivot:
            i += 1
            if(i == r): break
        while a[j] >= pivot :
            j -= 1
            if(j == l): break
        if i < j :
            a[i], a[j] = a[j], a[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j

def quicksort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        quicksort(a, low, pivot-1)
        quicksort(a, pivot+1, high)

T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(str,input().split()))
    dict_data = list(enumerate(data))
    print(gruop(dict_data))