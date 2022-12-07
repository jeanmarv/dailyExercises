def pig_it(text):
    # final = ""
    x = text.split(" ")
    # for i in x:
    #     if(i != "!" and i != "?"):
    #         final += (i[1:]+i[0]+"ay ")
    #     else:
    #         final += i
    # if(final[-1] == " "):
    #     return final[:-1]
    # return final
    for word in x:
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in x])

print(pig_it('Pig latin is cool'))