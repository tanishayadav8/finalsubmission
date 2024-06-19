str1=str(input("enter any string: "))


freq = {}

for i in str1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

