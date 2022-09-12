#WAP to find number of digits entered by a user



num = int(input("Enter a number: "))
count = 0
while num>0:
    count = count +1
    num = num//10

else:
    print("No of digits: ",count)
