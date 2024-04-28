# Jordan Houston-Taylor
# April 14, 2024
# P4HW2 Assignment
# To build off a previous assignment and use loop commands to calculate pay of employees based on the hours worked.

def calculate_pay(rate, hours):
    if hours <= 40:
        regular_pay = rate * hours
        overtime_pay = 0
        ot_hours = 0
        ot_pay = 0
    else:
        regular_pay = rate * 40
        ot_hours = hours - 40
        ot_pay = ot_hours * rate * 1.5
        overtime_pay = ot_pay
    gross_pay = regular_pay + overtime_pay
    return regular_pay, overtime_pay, ot_hours, ot_pay, gross_pay

# Variables to store totals
total_regular_pay = 0
total_overtime_pay = 0
num_employees = 0

while True:
    employee_name = input("Enter employee's name or 'Done' to terminate: ")
    if employee_name.lower() == "done":
        break

    hours_worked = float(input("How many hours did {} work? ".format(employee_name)))
    pay_rate = float(input("What is {}'s pay rate? ".format(employee_name)))
    
    regular_pay, overtime_pay, ot_hours, ot_pay, gross_pay = calculate_pay(pay_rate, hours_worked)
    
    # Update totals
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    num_employees += 1


    print("\nEmployee Name:", employee_name)



    # Display headings
    print("\n{:<15} {:<12} {:<12} {:<20} {:<15} {:<12}".format("Hours Worked", "Pay Rate", "OverTime", "OverTime Pay", "RegHour Pay", "Gross Pay"))
    print("-------------------------------------------------------------------------------------------")

    # Display calculations
    print("{:<15.1f} {:<12.2f} {:<12.1f} {:<19.2f} ${:<14.2f} ${:<11.2f}".format(hours_worked, pay_rate, ot_hours, ot_pay, regular_pay, gross_pay))

    print()
    
# Display totals based on employees inputted
print("\nTotal number of employees entered: {}".format(num_employees))
print("Total amount paid for overtime: ${:.2f}".format(total_overtime_pay))
print("Total amount paid for regular hours: ${:.2f}".format(total_regular_pay))
print("Total amount paid in gross: ${:.2f}".format(total_regular_pay + total_overtime_pay))

