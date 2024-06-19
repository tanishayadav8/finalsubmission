num=int(input("enter any number: "))



sum=int(0)

while num>0:
    rem = int(num % 10)
    quo = int(num / 10)
    sum=sum+rem

    num=quo

print(sum)


