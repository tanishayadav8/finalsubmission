import csv

with open('C:/Users/Tanisha Yadav/Documents/python ml/secondfile.csv','r') as file:
    reader=csv.reader(file, delimiter='|', skipinitialspace=True) #by specifying delimiter, it is gone. we are saying it is just a delimiter so it is then removing it and giving the output in form of actual format


    for row in reader:
        print(row)