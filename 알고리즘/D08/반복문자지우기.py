#테트리스처럼 스택쌓아서 풀기
import sys
sys.stdin = open("반복문자지우기.txt")
# sys.stdin = open("test.txt")

#추가함수
def push(str):
	ans.append(str)

#삭제함수
def pop():
    #ans 크기 확인 하기
    if len(ans) == 0:
        print("Stack is Empty!")
        return
    #삭제 두번하기
    else:
        ans.pop(-1)
        return ans.pop(-1)

T=int(input())

for tc in range(T):
    data =str(input())
    ans = []

    for i in range(len(data)):
        #스택(ans)에 추가
        push(data[i])
        #스택안의 갯수가 2개이상이고, 마지막에 추가된것과 바로 이전에 추가된것이 같은지 여부 확인
        if len(ans) > 1 and ans[-1] == ans[-2]:
            #반복문을 통해 지속적으로 확인하면서 삭제
            while len(ans) > 1 and ans[-1] == ans[-2]:
                pop()

    print("#{} {}".format(tc+1, len(ans)))