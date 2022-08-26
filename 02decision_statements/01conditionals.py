'''
Conditional Rendering
It allows us to make the decsion in the programs

only if
if else pair -> else will always come in pair with if
if elif ladder

nested if

indentation : It is providing spaces
to mention a scope or to have a block we use indentation
'''

# TODO: only if
'''
if condition:
    //if statments
'''

# age = int(input("Enter your age: "))
# print(type(age))
# print(age < 18)

# if age >=18 :
#     print("it is a part of if block")
#     print("You can vote !")

# print("It is not a part of if block")
# TODO: if else pair
'''
if condition:
    //if statments
else:
    //else statements
'''

# age = int(input("enter your age: "))

# if age >= 18:
#     print("You can vote !")
# else :
#     print("You cannot vote !")


# TODO: WAP to find whether you can drive or not
# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You can drive!")
# else:
#     print("You cannot drive!")


# TODO: WAP to find whether a given num is divisible by 5

# num = int(input("Enter the num : "))

# if num % 5 == 0:
#     print("Num is divisible by 5")
# else:
#     print("Num is not divisible by 5")


# TODO: WAP to find whether a given num is +ve/ -ve

# num = int(input("Enter a num: "))

# if num < 0 :
#     print("It is a negative number")
# else:
#     print("It is a positive number")



# TODO: WAP to find whther given no is even or odd

# num = int(input("Enter a num: "))

# if num % 2 == 0:
#      print(num , " is even number ")
# else:
#     print(num ," is odd number")


'''
if elif ladder

when we need to check more than one 
condition than we use if elif
'''


# TODO: WAP to find whether a given num is +ve/ -ve / 0

# num = int(input("Enter a num: "))

# if num > 0 :
#     print("It is a positive number")
# elif num == 0 :
#     print("It is zero")
# elif num < 0 :
#     print("It is a negative number")

# TODO: Grading system
# marks = float(input("Enter the marks: "))

# if marks > 90 and marks <= 100:
#     print("GRADE : A+")
# elif marks > 80 :
#     print("GRADE : A")
# elif marks >70:
#     print("GRADE: B+")
# elif marks > 60:
#     print("GRADE : C")
# elif marks > 50:
#     print("GRADE : D")
# elif marks >40:
#     print("GRADE : E")
# elif marks <=40 and marks>=0:
#     print("GRADE : F")
# else:
#     print("Enter a valid number")



# TODO: Feedback system 
# It will rating between 1-5 and you have to provide a msg for each rating

# rating = int(input("enter the rating: "))


# if rating == 5:
#     print("Awesome")
# elif rating == 4:
#     print("Good")
# elif rating == 3 :
#     print("Average")
# elif rating == 2:
#     print("need improvement")
# elif rating == 1:
#     print("Poor service")
# else:
#     print("Enter rating between 1-5")

# TODO : these are independent from each other
# if rating == 5:
#     print("Awesome")

# if rating == 4:
#     print("Good")

# if rating == 3 :
#     print("Average")
# else:
#     print("Poor: It is linked with rating==3 if")





# TODO: Nested if else
'''
if condition:
    if condition:
        // if statement
    else:
        // else statement
else:
    if condition:
        //if statement

'''

# TO make online purchase you must be logged in
# have added some item in the cart
# card details should correct

is_loggedin = True
is_cart = True
is_card = True

if is_loggedin:
    if is_cart:
        if is_card:
            print("Order placed successfully")
        else:
            print("Order didn't placed, check card details")
    else:
        print("Cart is empty")
else:
    print("Please login")


if is_loggedin and is_cart and is_card:
    print("Order placed successfully")
else:
    print("Check the details")