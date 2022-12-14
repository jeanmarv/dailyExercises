def generate_hashtag(s):
    if s != "" and len(s) < 140:
        return "#" + ''.join(s.capitalize().title().split(' '))
    return False
//
        output = "#"

    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output
//
    ans = '#'+ str(s.title().replace(' ',''))
    return s and not len(ans)>140 and ans or False


print(generate_hashtag("Hello tHere thanks for trying my Kata"))