def push(item):
    s.append(item)


def pop():
    if len(s) == 0:
        print("Stack is Empty!")
        return
    else:
        return s.pop(-1)

#
# def test(stack):
#     cnt = 0
#     for i in range(len(stack)):
#         if i == '(':
#             push('(')
#             cnt += 1
#
#         elif i == ')':
#             if s != []:
#                 pop()
#                 cnt -=1
#             else:
#                 return False
#     if cnt != 0:
#         return False
#
#     return True




#
#
# s = []
#
# print(test('()()((()))'))
# print(test('((()((((()()((()())((())))))'))


def check_matching(data):
    for i in range(len(data)):
        if data[i] == "(":
            push(data[i])
        