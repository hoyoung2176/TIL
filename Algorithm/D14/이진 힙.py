import sys
sys.stdin = open("이진 힙.txt")
def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index

    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)


T = int(input())
for tc in range(T):
    N = int(input())
    temp = list(map(int,input().split()))
    addr = [0 for _ in range(N+1)]
    i = 0

    inorder(1)
    last = addr[-1]
    enq(last)
    print(addr)