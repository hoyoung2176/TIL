def itoa(x):
    str = list()
    i, y = 0 , 0
    while True:
        y = x% 10
        str.append(chr(y+ord('0'))) #chr은 아스키코드 값을 문자로 리턴하는 함수
        x //= 10
        if x == 0:
            break
        i += 1
    str.reverse()
    str="".join(str)
    return str

x =123
print(x, type(x))
str1 = itoa(x)
print(str1, type(str1))