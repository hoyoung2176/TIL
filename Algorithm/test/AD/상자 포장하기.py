def DFS(no, Aarr, Barr, hap):
    global sol

    if no >= N:
        if sol < hap:
            sol = hap
        return

    if Aarr >= arr[no]:
        Aarr = arr[no]
        hap += arr[no]
    DFS(no + 1, Aarr, Barr, hap)
    if Aarr <= arr[no]:
        Aarr = arr[no]
        hap -= arr[no]
    if Barr <= arr[no]:
        Barr = arr[no]
        hap += arr[no]
    DFS(no + 1, Aarr, Barr, hap)
    if Barr >= arr[no]:
        Barr = arr[no]
        hap -= arr[no]
    DFS(no + 1, Aarr, Barr, hap)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    sol = 0

    DFS(0, 1000, 0, 0)
    print(sol)