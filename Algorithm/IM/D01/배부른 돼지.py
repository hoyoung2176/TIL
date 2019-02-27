import sys
sys.stdin = open("배부른 돼지.txt")

T =int(input())
min_food = 10
max_food = 0
if T == 0
    print('F')
else:
    for tc in range(T):
        num, result = map(str, input().split())
        if result == 'Y':
            if int(num) < min_food:
                min_food = int(num)
        else:
            if int(num) > max_food:
                max_food = int(num)

    if min_food < 10 and max_food > 0 and max_food < min_food:
        print(min_food)
    else:
        print('F')