import sys
sys.stdin = open("그릇.txt")

# data = input()
# ans = 0
# for i in range(len(data)):
#     if i == 0:
#         ans += 10
#     elif data[i] == '(':
#         if data[i-1] == '(':
#             ans += 5
#         else:
#             ans += 10
#     elif data[i] == ')':
#         if data[i-1] == '(':
#             ans += 10
#         else:
#             ans += 5
#
# print(ans)

data = input()
ans = 10
for i in range(1, len(data)):
    if data[i] == data[i-1]:
        ans += 5
    else:
        ans += 10
print(ans)