# Jordan Houston-Taylor
# March 24, 2024
# P3HW2 Assignment
# This assignment allows me to practice if/else codes, and spacing/formatting in Python. 


def calculate_pay(hours_worked, pay_rate):
    if hours_worked > 40:
        regular_pay = 40 * pay_rate
        ot_hours = hours_worked - 40
        ot_pay = ot_hours * (1.5 * pay_rate)
        gross_pay = regular_pay + ot_pay
    else:
        regular_pay = hours_worked * pay_rate
        ot_hours = 0
        ot_pay = 0
        gross_pay = regular_pay
    return regular_pay, ot_hours, ot_pay, gross_pay

def main():
    # Input
    employee_name = input("Enter employee's name: ")
    hours_worked = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))


    print("----------------------------------------------------------")


    # Calculation
    regular_pay, ot_hours, ot_pay, gross_pay = calculate_pay(hours_worked, pay_rate)

    # Output
    print("\nEmployee Name: ", employee_name)
    
    print("{:<15} {:<12} {:<12} {:<20} {:<20} {:<12}".format("Hours Worked", "Pay Rate", "OverTime", "OverTime Pay", "RegHour Pay", "Gross Pay"))
    print("----------------------------------------------------------------------------------------------")
    print("{:<15} {:<12} {:<12} {:<20.2f} ${:<19.2f} ${:<11.2f}".format(hours_worked, pay_rate, ot_hours, ot_pay, regular_pay, gross_pay))

if __name__ == "__main__":
    main()
