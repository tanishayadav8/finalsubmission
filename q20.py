list1=[]

n=int(input("no. of elements in list: "))

i=int(0)

while i<n:
    element=int(input("enter element: "))
    list1.append(element)

    i=i+1

print(f"{list1} is the list you have entered")

j=int(0)
sum=int(0)

while j<n:
    sum=sum+list1[j]

    j=j+1

print(f"sum of all elements of entered list is {sum}")
