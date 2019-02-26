def atoi(string):
    value = 0
    i = 0
    while (i < len(string)):
        c = string[i]
        if c >= '0' and c <= '9':
            digit = ord(c) - ord('0') #ord는 아스키코드 번호 (49-48), (50-48), (51-48) 등 아스키코드로 비교한다.
        else:
            break
        value = (value * 10) + digit;
        i += 1
    return value

a = '123'
print(type(a))
b = atoi(a)
print(type(b))
c = int(a)
print(type(c))