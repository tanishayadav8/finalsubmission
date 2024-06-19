unit=str(input("enter the units of input temperature (cel or fah): "))

temp=int(input("enter temperature: "))

if unit=='cel':
    fah=int((temp*9)/5+32)
    print(f"{temp} degree celcius = {fah} degree fahrenheit")

else:
    cel=int((temp-32)*5/9)
    print(f"{temp} degree fahrenheit = {cel} degree celcius")