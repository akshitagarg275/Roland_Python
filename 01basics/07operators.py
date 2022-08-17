'''
operators -> to perform operations
unary operator -> It requires one operand
binary operator -> It requires two operands
    -arithmetic 
    -assignment
    -relational
    -logical
    -bitwise operator
membership operator
identity operator

'''

# TODO : unary operator
# It tells whether the number is +ve/-ve
# a  = -5

'''
Arithmetic operator
+,-,/,* 
// -> floor divison
% -> modulus
** -> exponentation
'''

num1 = 5
num2 = 2

# add = num1+ num2
# print("Addition res is: ",add)

# sub = num1 - num2
# print("Subtraction res is: ",sub)


# mul = num1*num2
# print("Multiplication res is: ",mul)

# div = num1/num2
# print("Quotient res is: ",div)

# NOTE: floor division(//) gives quotient without decimal part
# print(num1 // num2)

# NOTE: modulus (%) is used to get the remainder
# print(num1%num2)

# print(5 ** 2)

# TODO: assignment operator '='

a = 2

# a = a + 3
# a += 3

# a = a * 5
# a *= 5

# print(a)


# TODO: Relational operator
'''
It is also known as comparison operator
It returs either True/False as the output
> - greater than
< - less than
>= - greater than equal to
<= - less than equal to

If left hand side value is either greater/less than or equal to right hand side value 
than it returns True

== - equal to (It checks if two values are equal)
!= - not equal to
'''

# print (5 > 3)
# print(6 < 4)

# print(5 >= 3)
# print( 5 >= 5)

# print( 6 <= 7)
# print ( 6<=3)

# print(5 == 5)
# print (5 = 5)

# print ( 5 != 5)


# TODO: Logical Operator
'''
and -> If anyone input is False output will be False

or -> If anyone input is True output will be True

not -> It reverses the state 

Falsy value -> False , None , '' , 0

'''

# print (5>3 and 4<3)
# print (5>3 or 4<3)

# print( not 0)

# print(not -5)

'''
Login methods
is_email
is_google
is_facebook
'''

is_email = True
is_google = False
is_facebook = False

# print(is_email or is_facebook or is_google)


# TODO: Bitwise operators
'''
these work on individual bits

& -> bitwise and
| -> bitwise or
^ -> bitwise xor
<< -> left shift -> It increases the bits
>> -> right shift -> It decreases the bits

'''

n1 = 7
# print(bin(n1))

n2 = 10

# print(n1 & n2)
# print(n1 | n2)
# print(n1 ^ n2)

# print(5<<1)
# print(5>>2)


# TODO: Membership operator (in)
# nums = [1,2,3,4,5]
# print( 1 in nums)
# print( 6 in nums)

# print(11 not in nums)

# name = "Harry"
# print( 'H' in name)

# TODO: Identity operator (is)
# It checks if two variables are at same memory address or not

a = 10
# print(id(a))

b = 10
# print(id(b))

# print(a is b)

