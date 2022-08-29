'''
DRY -> Donot Repeat Yourself

while
for

It allows to do a certain task without rewriting the code

while loop

initialization
condition
updation (re-initialization)
'''

# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")

# i = 1
# while i <=5 :
#     print("Hello: ",i)
#     i=i+1


# TODO: reverse counting from 10-1

# i = 10

# while i >= 1:
#     print(i)
#     i=i - 1


# TODO: Infinite loop ->  a loop which necer stops
# while True:
#     print("Infinite")


# TODO: WAP to find even numbers from 0-10

# i = 0

# while i <= 10:
#     if i%2 == 0:
#         print(i)
#     i = i + 1


# TODO: WAP to find sum of first n numbers
# n = 5
# 1+2+3+4+5 =15

# n = 3
# 1+2+3 = 6

# num = int(input("Enter a num: "))

# i = 1
# sum = 0
# while i <= num:
#     sum = sum + i
#     i = i + 1

# print("The sum of nums is :",sum)


# TODO: WAP to find multiplication of first n numbers
# n = 5
# 1*2*3*4*5 =120

# n = 3
# 1*2*3 = 6

# num = int(input("Enter a num: "))

# i = 1
# mul = 1
# while i <= num:
#     mul = mul * i
#     i = i + 1

# print("The mul of nums is :",mul)


'''
for loops
for loops are used on iterables(list, tuple , range, dictionary)
'''

nums = [11,22,33,44,55,66,77]

for i in nums:
    print(i)