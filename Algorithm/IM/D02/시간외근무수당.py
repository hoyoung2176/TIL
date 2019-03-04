import sys
sys.stdin = open('시간외근무수당.txt')
week_ow = 0
pro_pay = 0
for i in range(5):
    s, e = map(float, input().split())
    ow = e - s -1
    if ow > 0 and ow <= 4:
        week_ow += ow
        pro_pay += ow / 0.5 * 5000
    elif ow > 4:
        ow = 4
        week_ow += ow
        pro_pay += ow / 0.5 * 5000
    elif ow <= 0:
        ow = 0

if week_ow >= 15:
    print(int(pro_pay-(pro_pay//100*5)))
elif week_ow <= 5:
    print(int(pro_pay+(pro_pay//100*5)))
else:
    print(int(pro_pay))