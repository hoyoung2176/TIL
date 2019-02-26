str1 = '2+3*4/5'
str2 = []
stack = []

for i in str1:
    if i.isdigit():
        str2.append(i)
    else:
        stack.append(i)

for i in range(len(stack)):
    str2+=stack.pop()
print(''.join(str2))
