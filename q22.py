index=int(input("enter no. of elements in a list: "))
list1=[]

i=int(0)

while i<index:
    num=int(input(f"enter {i}th element of list: "))
    n=list1.append(num)
    i=i+1


max=int(list1[0])

j=int(1)

while j<index:
    if max<list1[j]:
        max=list1[j]

    j=j+1

print(f"{max} is the maximum value entered in the list")




min=int(list1[0])

k=int(1)

while k<index:
    if min>list1[k]:
        min=list1[k]

    k=k+1

print(f"{min} is the minimum value entered in the list")

