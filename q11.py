num=int(input("enter any number till where you want fibonacci series: "))

n1 = 0
n2=1
count = 0


if num <= 0:
   print("Please enter a positive integer")

elif num == 1:
   print(n1)

else:
   while count < num:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

