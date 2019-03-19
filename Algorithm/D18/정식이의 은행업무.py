import sys
sys.stdin = open("정식이의 은행업무.txt")

def binarychange(n):
    ans = 0
    for i in range(len(n)):
        ans += int(n[i]) * (2**(len(n)-i-1))
    return ans

def ternarychange(n):
    ans = 0
    for i in range(len(n)):
        ans += int(n[i]) * (3 ** (len(n) - i - 1))
    return ans


T = int(input())
for tc in range(T):
    binary_num = input()
    ternary_num = input()

    sol = 0
    flag = 0
    for i in range(len(binary_num)):
        binary_list = list(binary_num)
        if binary_list[i] == '1':
            binary_list[i] = '0'

        else:
            binary_list[i] = '1'

        binary_T = binarychange(binary_list)

        for j in range(len(ternary_num)):
            ternary_list = list(ternary_num)
            if ternary_list[j] == '0':
                ternary_list[j] = '1'
                if binary_T == ternarychange(ternary_list):
                    sol = binary_T
                    flag = 1
                    break
                ternary_list[j] = '2'
                if binary_T == ternarychange(ternary_list):
                    sol = binary_T
                    flag = 1
                    break
            elif ternary_list[j] == '1':
                ternary_list[j] = '0'
                if binary_T == ternarychange(ternary_list):
                    flag = 1
                    sol = binary_T
                    break
                ternary_list[j] = '2'
                if binary_T == ternarychange(ternary_list):
                    flag = 1
                    sol = binary_T
                    break
            elif ternary_list[j] == '2':
                ternary_list[j] = '1'
                if binary_T == ternarychange(ternary_list):
                    flag = 1
                    sol = binary_T
                    break
                ternary_list[j] = '0'
                if binary_T == ternarychange(ternary_list):
                    flag = 1
                    sol = binary_T
                    break


        if flag == 1:
            break
    print("#{} {}".format(tc+1, sol))
