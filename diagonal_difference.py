def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    leng = len(arr)
    for i, row in enumerate(arr):
        iminus = (leng -i) -1
        sum1 += arr[i][i]
        sum2 += arr[i][iminus]
    return abs(sum1 - sum2)