def timeConversion(s):
    last_element = s[-2]
    first_two = s[0:2]
    all_rest = s[2:-2]
    final_result = first_two + all_rest
    if last_element == "P" and first_two == "12":
        return final_result
    if last_element == "A" and first_two == "12":
        first_two = int(first_two) - 12
        first_two = str(first_two) + "0" + all_rest
        return first_two
    if last_element == "P":
        first_two = int(first_two) + 12
        first_two = str(first_two) + all_rest
        return first_two
    return final_result


string = ("12:40:22AM")
print (timeConversion(string))

# last_element = string[-2]
# string2 = string[0:2]
# string3 = string[2:-2]
# string4 = int(string2) + 12
# string4 = str(string4) + string3
# print(string4)

