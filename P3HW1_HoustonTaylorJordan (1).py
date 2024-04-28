# Jordan Houston-Taylor

# March 12, 2024

# P3HW1 Debug Assignment

# This assignment will help me practice debug incorrect codes in python




# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades

lowest_grade = min(grades)
highest_grade = max(grades)
total_of_grades= sum(grades)
average_grade = total_of_grades/ len(grades)

print("--------------Results--------------")

print(f"Lowest Grade:    {lowest_grade:.1f}")
print(f"Highest Grade:   {highest_grade:.1f}")
print(f"Sum of Grades:   {total_of_grades:.1f}")
print(f"Average:         {average_grade:.2f}")
#Display the results with proper formatting and correct allignment where the outputs look like an even column

print("-----------------------------------")

# determine letter grade for average

if avg >= 90:
print('Your grade is: A')

else if average >= 80:
 print('Your grade is: B')

else if average >= 70:
 print('Your grade is: C')

else if average >= 60:
 print('Your grade is: D')

else if average >= 50:
print('Your grade is: F')



# TO DO: finish this





