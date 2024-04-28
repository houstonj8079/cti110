#Jordan Houston-Taylor

#March 10,2024

#P2HW2 Assignment

#This assignment will help me learn how to use the Python methods I have learned thus far .

#Creates an empty list to store grades
grades_list = []
for the module in range(1, 7):
    grade = float(input(f"Enter grade for Module {module}: "))
    grades_list.append(grade)
#User will be asked to enter grades for each module and add them to the list

lowest_grade = min(grades_list)
#Calculation of the lowest grade in the list

highest_grade = max(grades_list)
#Calculation the highest grade in the list

sum_of_grades = sum(grades_list)
#Calculation of the sum of all grades in the list, add all grades together 

average_grade = sum_of_grades / len(grades_list)
#Calculation of the average of all grades in the list, add all grades together and then divide by 6

print("--------------Results--------------")

print(f"Lowest Grade:        {lowest_grade}")
print(f"Highest Grade:       {highest_grade}")
print(f"Sum of Grades:       {sum_of_grades}")
print(f"Average:             {average_grade:.2f}")
#Display the results with proper formatting and correct allignment where the outputs look like an even column

print("-----------------------------------")
