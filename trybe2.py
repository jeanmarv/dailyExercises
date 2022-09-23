def countMoves(numbers):
    sorted_numb = sorted(numbers)
    while sorted_numb[0] != sorted_numb[-1]:
        sorted_numb[0] += 1
        sorted_numb[1] += 1
        sorted_numb[2] += 1
        sorted_numb[3] += 1
        sorted_numb = sorted(sorted_numb)
    return sorted_numb

print(countMoves([1, 5, 3, 2, 4]))