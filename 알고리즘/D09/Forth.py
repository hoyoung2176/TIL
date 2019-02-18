import sys
sys.stdin = open("Forth.txt")

T =int(input())

for tc in range(T):
    data = list(map(str, input().split()))
    stack = []
    result = str()
    for i in range(len(data)):
        if data[i].isdigit():
            stack.append(data[i])
        elif len(stack) > 2 and data[i]=='+':
            b=int(stack.pop())
            a=int(stack.pop())
            stack.append(a+b)
        elif len(stack) > 2 and data[i] == '-':
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif len(stack) > 2 and data[i] == '*':
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        elif len(stack) > 2 and data[i] == '/':
            b = stack.pop()
            a = stack.pop()
            stack.append(a / b)
        else:
            result = 'error'

    if result == 'error':
        print('error')
    else:
        print(stack)

