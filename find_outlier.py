def find_outlier(integers):
#     counter = 0
#     evenn = 0
#     odds = 0
#     for i in integers:
#         if (i%2==0):
#             counter += 1
#             evenn = i
#         if (i%2==1):
#             odds = i
#     if counter == 1:
#         return evenn
#     else:
#         return odds
    # odds = [x for x in integers if x%2!=0]
    # print(odds)
    # evens= [x for x in integers if x%2==0]
    # print(evens)
    # return odds[0] if len(odds)<len(evens) else evens[0]
    parity = [n % 2 for n in integers]
    print(parity)
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]

print (find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))