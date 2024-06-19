str1=str(input("enter string1: "))
str2=str(input("enter string2: "))

any=int(0)
i=int(0)
j=int(0)

if len(str1)!=len(str2):
    print("they are not anagrams of each other")



else:
    while i<len(str1):
        j=0
        while j<len(str2):
            if str1[i] == str2[j]:
                any=any+1
                break
            j=j+1

        i=i+1


    if any==len(str1):
        print("they are anagrams of each other")

    else:
        print("they are not anagrams of each other!")