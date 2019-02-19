"""
예외 사항
data . 안찍는 경우
2개이상 못꺼내서 계산 못하는경우
stack에 1개이상의 정보가 담긴경우
나눗셈은 정수로만 표현

"""

import sys
sys.stdin = open("Forth.txt")

T =int(input())

def calculator(i, data):
    global stack
    if data[i] == '+':
        b = int(stack.pop())
        a = int(stack.pop())
        stack.append(a + b)
    elif data[i] == '-':
        b = int(stack.pop())
        a = int(stack.pop())
        stack.append(a - b)
    elif data[i] == '*':
        b = int(stack.pop())
        a = int(stack.pop())
        stack.append(a * b)
    elif data[i] == '/':
        b = int(stack.pop())
        a = int(stack.pop())
        stack.append(a // b)

for tc in range(T):
    data = list(map(str, input().split()))
    stack = []
    for i in range(len(data)):
        if data[i].isdigit():
            stack.append(data[i])
        elif len(stack) >= 2 and data[i].isdigit() == False:
            calculator(i, data)
        else:
            break


    if len(stack) == 1 and data[i] == '.':
        print('#{} {}'.format(tc+1, stack[0]))
    else:
        print('#{} error'.format(tc + 1))

