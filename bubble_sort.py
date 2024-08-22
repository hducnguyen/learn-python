def bubble (list):
    index_Length = len(list) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, index_Length):
            if list[i]> list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]
    return list

print(bubble([5, 8, 3, 7, 9]))