def to_camel_case(text):
    final_text = ""
    for row, i in enumerate(text):
        if (i != "-" and i != "_" and text[row-1] != "-" and text[row-1] != "_"):
            final_text += i
        if (i == "-" or i == "_"):
            final_text += text[row+1].upper()
    return final_text
print(to_camel_case("the-stealth-warrior"))

    words = text.replace('_', '-').split('-')
    return words[0] + ''.join([x.title() for x in words[1:]])