#WAP to find number of digits entered by a user

# num = int(input("Enter a number: "))
# count = 0
# while num>0:
#     count = count +1
#     num = num//10

# else:
#     print("No of digits: ",count)


# WAP to add all the digits entered by the user
# 564 -> 5 + 6 + 4 = 15
# 123 -> 1 + 2 + 3 = 6


# num = int(input("Enter a num :"))
# sum = 0

# while num > 0 :
#     rem = num % 10
#     sum = sum + rem
#     num = num // 10

# print("Sum of digits is: ",sum)
 

# WAP : to reverse a given number
# 564 -> 465

num = int(input("Enter a num :"))
rev= 0

while num > 0 :
    rem = num % 10
    rev = (rev * 10 ) + rem
    print("Inside: ",rev)
    num = num //10

print("Reverese is :",rev)