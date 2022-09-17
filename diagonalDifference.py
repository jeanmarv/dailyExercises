def diagonalDifference(arr):
    sum1 = arr[0][0] + arr[1][1] + arr[2][2]
    sum2 = arr[2][0] + arr[1][1] + arr[0][2]
    allsum = (sum1 - sum2)
    return abs(allsum)