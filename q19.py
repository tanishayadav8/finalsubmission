def remove_commas(string):
    result = ""
    for char in string:
        if char != ",":
            result += char
    return result


input_str=str(input("enter any string: "))
output_str = remove_commas(input_str)
print(output_str)