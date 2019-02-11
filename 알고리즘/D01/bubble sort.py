def BubbleSort(data):
    for i in range(len(data)-1, 0, -1): # 4 3 2 1
        for j in range(0, i): # 4 3 2 1
            if data[j] > data[j+1]: #부등호만 바꾸면 오름차순 내림차순 바뀐다.
                data[j], data[j+1] = data[j+1], data[j] #큐플타입, 스왑
    return
data=[55,7,78,12,42]#리스트는 함수로 가면 바뀔수있다. (레퍼런스타입은)
                    #일반변수 data=1이면 안바뀜

BubbleSort(data)

print(data)