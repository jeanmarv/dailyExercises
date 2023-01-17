from collections import Counter

# a = [1, 2, 3, 4, 3, 2, 1]

# bc = Counter(a).most_common()
# print(bc[-1][0])

def lonelyinteger(a):
    count = Counter(a).most_common()
    return (count[-1][0])

a = [1, 2, 3, 4, 3, 2, 1]
print(lonelyinteger(a))