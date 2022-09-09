def plusMinus(arr):
    somatorioPos = 0
    somatorioZero = 0
    somatorioNegative = 0
    print (somatorioPos)
    print (somatorioNegative)
    for i in arr:
        if i > 0:
            somatorioPos += 1
        if i == 0:
            somatorioZero += 1
        if i < 0:
            somatorioNegative += 1
    allArray = [somatorioPos / len(arr), somatorioNegative / len(arr) , somatorioZero / len(arr)]
    return allArray

    print(plusMinus([1,2,3,4,5]))