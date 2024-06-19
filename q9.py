string=input("please enter any string: ")
str2=input("Please any sub-string you wish to check whether it is there in parent literal or not: ")

if str2 in string:
    print(f"'{str2}' is present in '{string}'")

else:
    print(f"'{str2}' is not present in '{string}'")