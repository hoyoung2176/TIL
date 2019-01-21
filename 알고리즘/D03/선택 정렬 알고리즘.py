
def seletionSort(a):
    for i in range(0, len(a) - 1):  # 최소값 찾는 횟수
        min = i
        for j in range(i + 1, len(a)):  # 최소값찾음
            if a[min] > a[j]:
                min = j
            a[i], a[min] = a[min], a[i]  # 스왑

data = [64, 25, 10, 22, 11]
seletionSort(data)
print(data)