# Jordan Houston-Taylor

# March 12, 2024

# P3LAB Assignment

# This assignment is for me to practice to correctly branch in Python.


is_leap_year = False
   
input_year = int(input())

if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
    is_leap_year = True

if is_leap_year:
    print(f"{input_year} - leap year")
    
else:
    print(f"{input_year} - not a leap year")
