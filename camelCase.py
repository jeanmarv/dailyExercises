def solution(s):
    final = ""
    for i in s:
        if i == i.upper():
            final += " "
            final += i
        else:
            final += i
    return(final)

    return ''.join(' ' + c if c.isupper() else c for c in s)

print(solution("helloWorld"))