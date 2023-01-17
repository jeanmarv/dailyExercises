def plusMinus(arr):
    somatorioPos = 0
    somatorioZero = 0
    somatorioNegative = 0
    for i in arr:
        if i > 0:
            somatorioPos += 1
        if i == 0:
            somatorioZero += 1
        if i < 0:
            somatorioNegative += 1
    allArray = [somatorioPos / len(arr), somatorioNegative / len(arr) , somatorioZero / len(arr)]
    return allArray

print (plusMinus([-4, 3, -9, 0, 4, 1]))