# by ariana daney
# last modified october 17, 2019
# daily exercises unit 5

import random
# ex. 1

# print("make sure the numbers you enter make sense in order")
# user_upper = int(input("enter a upper number please"))
# user_lower = int(input("please enter a lower number"))
# for x in range(user_lower, user_upper + 1):
#     print(x)
# if user_lower > user_upper:
#     # the -1 includes the lowest number
#     for x in range(user_lower, user_upper - 1, - 1):
#         print(x)


# ex. 2
#
# for x in range(10, 21, 2):
#     print(x)
#

# ex. 3
# user_even = int(input("please enter a positive number"))
# for x in range(13):
#     print(user_even, "*", x, "=", user_even * x)


# ex. 4
# even_sum = 0
# odd_sum = 0
# for x in range(11):
#     num = random.randint(1, 101)
#     print(num)
#     if (num % 2) == 0:
#         even_sum = even_sum + num
#     else:
#         odd_sum = odd_sum + num
# print("the even numbers add to", even_sum)
# print("the odd numbers add to", odd_sum)


# ex. 5
# multiples = 0
# for x in range(3, 1000):
#     if (x % 3) == 0 or (x % 5) == 0:
#         multiples = multiples + x
# print("the sum of all the multiples of 3 and 5 between 1 and 1000 are", multiples)


# ex. 6
# x = 0
# user_num = int(input("please enter a number"))
# while x < user_num + 1:
#     print("* " * x)
#     x = x + 1


# ex. 7
# tries = 0
# total = 0
# product = 1
# while True:
#     user_guess = input("enter a number")
#     if user_guess == "q":
#         break
#     user_guess = int(user_guess)
#     tries += 1
#     total = total + user_guess
#     product = product * user_guess
# print("the average of your numbers is", total / tries, "and the product is", product)


# ex. 8
num = int(input("please enter a number"))
steps = 0
while num != 1:
    if (num % 2) == 0:
        even = num / 2
        print(num, "->", num, "/2 =", even)
        num = even
    else:
        odd = num * 3 + 1
        print(num, "->", num, "* 3 + 1 =", odd)
        num = odd
    steps += 1
print("it took you", steps, "steps to get to 1")
