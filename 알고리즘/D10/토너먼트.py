#분할정렬
import sys
sys.stdin = open("토너먼트.txt")

def battle(a, b):
    global lose_dict
    if a[1] == b[1]:
        return a
    elif a[1] == lose_dict[b[1]]:
        return a
    elif lose_dict[a[1]] == b[1]:
        return b

def gumsa(data):
    global result
    stack = []
    i = 0
    if len(data) == 1:
        global tc
        # print("#{} {}".format(tc+1, data[0][0]+1))
        return data
    else:

        while i < len(data):
            stack += (data[i],)
            i += 1
            if len(stack) > 1:
                b = stack.pop()
                a = stack.pop()
                result += (battle(a, b),)
                return result

        # if len(result) % 2:
        #     result += stack
        #     # gumsa(result)
        #     return gumsa(result)
        # else:
        #     # gumsa(result)
        #     return gumsa(result)

def gruop(dict_data, low, high):
    # global result
    # if len(dict_data) > 2:
    #     if len(dict_data) % 2:
    #         group_01 = dict_data[0:len(dict_data) // 2+1]
    #         group_02 = dict_data[len(dict_data) // 2+1: len(dict_data)]
    #     else:
    #         group_01 = dict_data[0:len(dict_data)//2]
    #         group_02 = dict_data[len(dict_data)// 2 : len(dict_data)]
    #     gruop(group_01)
    #     gruop(group_02)
    # else:
    #     gumsa(dict_data)
    #
    # if len(result) >= 2:
    #     data_01 = result
    #     result = []
    #     gruop(data_01)
    # else:
    #     return result
#     if high > 2:
#         if high % 2:
#             partition(a, low, high)
#             pivot = high // 2 + 1
#             gruop(dict_data, low, pivot - 1)
#             gruop(dict_data, pivot + 1, high)
#         else:
#             pivot = high // 2
#             gruop(dict_data, low, pivot-1)
#             gruop(dict_data, pivot+1, high)
#     else:
#         gumsa(dict_data)
#
# def partition(a, low, high):


T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(str,input().split()))
    dict_data = list(enumerate(data))
    lose_dict = {'1' : '2', '2' : '3', '3' : '1'} #패배관계 딕셔너리 표현
    result = []
    # print(gruop(dict_data))

    print("#{} {}".format(tc+1, gruop(dict_data, 0, N)[0][0]+1))