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

def gumsa(dict_data, low, high):
    global result
    data = []
    for k in range(low, high+1):
        data += (dict_data[k],)
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
    #위치값만 변하게, low, high만 바꾼다.
    global result
    if (high - low) > 2:
        low_01, high_01 = (high)//2, (high//2-1)
        gruop(dict_data, low, high_01)
        gruop(dict_data, low_01, high)

    elif (high - low) == 2:
        gumsa(dict_data, low, high-1)

    elif (high - low) == 1:
        result += dict_data[low]

T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(str,input().split()))
    dict_data = list(enumerate(data))
    lose_dict = {'1' : '2', '2' : '3', '3' : '1'} #패배관계 딕셔너리 표현
    result = []
    gruop(dict_data, 0, len(dict_data))
    ans = result
    while len(ans) > 1:
        ans = result
        result = []
        gruop(ans, 0, len(ans)-1)
    print("#{} {}".format(tc+1, ans))