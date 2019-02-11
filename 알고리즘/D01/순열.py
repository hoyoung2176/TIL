def bayjin(data):
    for i1 in range(6): #len(data)+1 = 6
        for i2 in range(6):
            if i2 != i1 :
                for i3 in range(6):
                    if i3 != i1 and i3 != i2:
                        for i4 in range(6):
                            if i4 != i3 and i4 != i2 and i4 != i1:
                                for i5 in range(6):
                                    if i5 != i4 and i5 != i3 and i5 != i2 and i5 != i1:
                                        for i6 in range(6):
                                            if i6 != i5 and i6 != i4 and i6 != i3 and i6 != i2 and i6 != i1:
                                                chk = 0
                                                if data[i1] == data[i2] and data[i2] == data[i3]:
                                                    chk += 1
                                                if data[i4] == data[i5] and data[i5] == data[i6]:
                                                    chk += 1
                                                if data[i1] + 1 == data[i2] and data[i2] + 1 == data[i3]:
                                                    chk += 1
                                                if data[i4] + 1 == data[i5] and data[i5] + 1 == data[i6]:
                                                    chk += 1
                                                if chk == 2:
                                                    print("Baby-gin")
                                                    return

data=[6, 6, 7, 7, 6, 7]
bayjin(data)

