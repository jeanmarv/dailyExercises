def isPP(n):
    first_mult = 2
    last_mult = 2
    while first_mult < 30:
        print(f"this is first {first_mult}")
        print(f"this is last {last_mult}")
        if first_mult**last_mult == n:
            return [first_mult, last_mult]
            break
        last_mult += 1
        if last_mult == 30:
            first_mult += 1
            last_mult = 2
    return None

print (isPP(484))