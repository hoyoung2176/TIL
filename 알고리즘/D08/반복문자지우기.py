#테트리스처럼 스택쌓아서 풀기
import sys
sys.stdin = open("반복문자지우기.txt")
# sys.stdin = open("test.txt")
def push(str):
	ans.append(str)

def pop():
    if len(ans) == 0:
        print("Stack is Empty!")
        return
    else:
        ans.pop(-1)
        return ans.pop(-1)

T=int(input())

for tc in range(T):
    data =str(input())
    ans = []
    for i in range(len(data)):
        push(data[i])
        if len(ans) > 1 and ans[-1] == ans[-2]:
            while len(ans) > 1 and ans[-1] == ans[-2]:
                pop()

    print("#{} {}".format(tc+1, len(ans)))