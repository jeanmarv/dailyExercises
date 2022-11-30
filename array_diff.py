def two_sum(numbers, target):
    for row1, i in enumerate(numbers):
        for row2, i2 in enumerate(numbers):
            if(i + i2 == target and row1 != row2):
                lista = [row1, row2]
                return lista




print(two_sum([1,2,3], 4))