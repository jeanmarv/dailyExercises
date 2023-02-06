def create_phone_number(n):
    first = f'{n[0]}{n[1]}{n[2]}'
    second = f'{n[3]}{n[4]}{n[5]}'
    third = f'{n[6]}{n[7]}{n[8]}{n[9]}'
    result = f'({first}) {second}-{third}'
    return result
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

# return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)