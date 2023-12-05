"""
Program to multiply the user input whole number by multiple's of 2 and print it
"""

whole_num = int(input("Generate a multiplication table for: "))  # takes user input

print("_" * 10)  # prints 10 underscores at top border

print("Number:", whole_num)  # print Number

# for loop iterates from 2 to 10 with step of 2(step of 2 signifies multiples of 2)
for x in range(2, 11, 2):
    print(x, ": ", (x * whole_num), sep="")  # multiplies x by whole number and prints it

print("_" * 10)  # prints 10 underscore at bottom
