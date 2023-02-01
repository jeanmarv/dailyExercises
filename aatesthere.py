import math

def powerNumbers( n):
    v = []
    for i in range(2,
               int(math.pow(n, 1.0 /
                               3.0)) + 1) :
        j = i * i
        while (j * i <= n) :
             
            j = j * i
            s = int(math.sqrt(j))
            if (s * s != j):
                v.append(j)
    v.sort()
    v = list(dict.fromkeys(v))
    return len(v) + int(math.sqrt(n))
 
print (powerNumbers(300))