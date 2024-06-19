check=str(input("if you want to check for suffix then enter 's' else enter 'p': "))
str1=str(input("enter the parent string: "))


if check=='s':
    suffix = str(input("enter suffix if any: "))
    lens = int(input("enter no. of letters in suffix: "))

    if suffix not in str1:
        print("suffix isnt present")

    else:
        if str1[lens-1:]==suffix:
            print("given suffix is present in string")

        else:
            print("suffix isnt present in string")


else:
    prefix = str(input("enter prefix if any (if no then enter 0)"))
    lenp = int(input("enter no. of letters in prefix: "))

    if prefix not in str1:
        print("prefix isnt present in string")

    else:
        if str1[:lenp-1]==prefix:
            print("given prefix is present in string")

        else:
            print("given prefix isnt present in string")






