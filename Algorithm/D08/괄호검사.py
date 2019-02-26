import sys
sys.stdin = open("괄호검사.txt")
# sys.stdin = open("test.txt")
T = int(input())

#삽입함수
def push(item):
    ans.append(item)

#제거함수
def pop():
    if len(ans) == 0:
        return
    else:
        return ans.pop(-1)

#비어있는 건지 여부 확인
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
            #{,(이면 스택에 넣기
            if data[i] == "{" or data[i] == "(":
                push(data[i])

            #}이면 이전에 스택에 쌓인거 확인
            elif data[i] == "}":
                #스택이 비어있는지 확인
                if Empty_list():
                    # ( 이면 종료시키고 0값을 보냄
                    if ans[-1] == "(":
                        return 0
                    else:
                        pop()
                else:
                    return 0
            # ) 이면 이전에 스택 쌓인거 확인
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