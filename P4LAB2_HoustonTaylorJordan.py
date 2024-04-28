# Jordan Houston-Taylor
# P4LAB2 Assignment
# April 7, 2024
# This assignment will help me test how to write programs with output ranges that have increments.

# input integers
num1 = int(input())
num2 = int(input())

# see if second integer is less than first
if num2 < num1:
    print("Second integer can't be less than the first.")
else:
    # output the first integer
    print(num1, end=' ')

    # output subsequent increments of 5 as long as the value is less than or equal to the second integer
    while num1 + 5 <= num2:
        num1 += 5
        print(num1, end=' ')

    print()
