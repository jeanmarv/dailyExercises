def multiples(number):
    sumat = 0;
    for i in range(number):
        if(i % 3 == 0 or i % 5 == 0):
            sumat += i
    return sumat;
print (multiples(-10))
