def descending_order(num):
    final_str = ""
    conver_str = str(num)
    sort_str = sorted(conver_str, reverse=True)
    for i in sort_str:
        final_str += i
    return int(final_str)

print(descending_order(158))

    # return int("".join(sorted(str(num), reverse=True)))