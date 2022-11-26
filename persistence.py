import math

def persistence(n):
    if n < 10:
        return 0
    stringfy = list(map(int, str(n)))
    counter = 1
    blau = math.prod(stringfy)
    while blau >= 10:
        blau = list(map(int, str(blau)))
        blau = math.prod(blau)
        counter += 1
    return counter

    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i

        n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count

print(persistence(25))