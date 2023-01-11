def snail(snail_map):
    last_resort = []
    while snail_map:

        for i in snail_map[0]:
            last_resort.append(i)
        snail_map.pop(0)

        if not snail_map:
            break

        for j in snail_map:
            last_resort.append(j[-1])
            j.pop()

        if not snail_map:
            break

        for k in snail_map[-1][::-1]:
            last_resort.append(k)
        snail_map.pop(-1)

        if not snail_map:
            break

        for l in snail_map[::-1]:
            last_resort.append(l[0])
            l.pop(0)

        if not snail_map:
            break

    return last_resort

//

import numpy as np

def snail(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m


print (snail([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10],[11, 12, 13, 14, 15],[16, 17, 18, 19, 20],[21, 22, 23, 24, 25]]))
