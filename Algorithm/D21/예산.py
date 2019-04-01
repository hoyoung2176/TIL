N = int(input())
temp = list(map(int, input().split()))
max_num = int(input())
temp.sort(reverse=True)
data = temp
over_num = sum(data)- max_num

while over_num >= 0:
    data[0] -= 1
    over_num -= 1
    data.sort(reverse=True)

print(max(data))