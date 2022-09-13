def miniMaxSum(arr):
    sortArr = sorted(arr)
    minSum = sum(sortArr) - sortArr[4]
    maxSum = sum(sortArr) - sortArr[0]
    print(minSum, maxSum)