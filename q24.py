num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
oper=str(input("enter operator (+,-,*,/): "))

if oper=='+':
    result=int(num1+num2)
    print(f"{num1}+{num2}={result}")


elif oper=='-':
    result = int(num1 - num2)
    print(f"{num1}-{num2}={result}")

elif oper=='*':
    result = int(num1 * num2)
    print(f"{num1}*{num2}={result}")

else:
    result = int(num1/num2)
    print(f"{num1}/{num2}={result}")
