def countingSort(arr):
    array_hundred = []
    return_array = []
    sum1 = 0
    while True:
        array_hundred.append(0)
        if len(array_hundred) > 99:
            break
    for i, row in enumerate(arr):
        num_in_array = row
        array_hundred[num_in_array] += 1
    # for i, row in enumerate(array_hundred): //this part was not needed, it was the final sort
    #     while True:
    #         if sum1 == row:
    #             break
    #         return_array.append(i)
    #         sum1 += 1
    #     sum1 = 0
    return array_hundred


print(countingSort([0, 1, 2, 3, 4, 1, 1, 5]))