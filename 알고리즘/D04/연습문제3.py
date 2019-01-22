
"""
9 20 2 18 11
19 1 25 3 21
8 24 10 17 7
15 4 16 5 6
12 13 22 23 14
"""
def iswall(x,y):
    if x<0 or x>=5:
        return True
    if y<0 or y>=5:
        return True

def row(arr,test,x):
    arr = [[0 for _ in range(5)] for _ in range(5)]
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            test += 1
            test_X = x+1
            test_Y = 0
            if iswall(test_X,test_Y) != True:
                arr[y][x] = test
            if iswall(test_X, test_Y) == True:
                arr[y][x] = test
                a = x
                return col(arr,test,y)

def col(arr,test,y):
    test_Y=0
    for x in range(len(arr[y])):
        test += 1
        test_X = 0
        test_Y += 1
        if iswall(test_X,test_Y) != True:
            arr[x][y] = test
        if iswall(test_X, test_Y) == True:
            arr[x][y] = test
            return row(arr,test,x)
arr=0
test=0
x=0
test=0
print(row(arr,test,x))

# for y in range(len(arr)):
#     for x in range(len(arr[y])):
#         test += 1
#         for i in range(4):
#             test_X = x+dx[i]
#             test_Y = y+dy[i]
#             if iswall(test_X,test_Y) != True:
#                 arr[x][y] = test


