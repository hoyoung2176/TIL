import sys
sys.stdin = open("괄호검사.txt")
# sys.stdin = open("test.txt")
T = int(input())

def push(item):
    ans.append(item)

def pop():
    if len(ans) == 0:
        return
    else:
        return ans.pop(-1)

def Empty_list():
    if len(ans) == 0:
        return 0
    else:
        return 1


for tc in range(T):
    data = str(input())
    ans = []
    def check_list(data):
        for i in range(len(data)):
            #중괄호검사
            if data[i] == "{" or data[i] == "(":
                push(data[i])

            elif data[i] == "}":
                if Empty_list():
                    if ans[-1] == "(":
                        return 0
                    else:
                        pop()
                else:
                    return 0

            elif data[i] == ")":
                if Empty_list():
                    if ans[-1] == "{":
                        return 0
                    else:
                        pop()
                else:
                    return 0

        if Empty_list():
            return 0
        else:
            return 1


    print("#{} {}".format(tc+1, check_list(data)))