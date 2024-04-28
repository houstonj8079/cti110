
# Jordan Houston-Taylor
# March 10, 2024
# P2HW1 Assignment
# The purpose of this project to build upon a previous python code that will be able to collect and process information using float inputs.

print("This program calculates and displays travel expenses\n")

user_budget = float(input("Enter Budget: "))
(f"Budget: ${user_budget:.2f}")
#user_budgt ← USER INPUT A

user_travel = input("\nEnter your travel destination: ")
(f"Travel Destination: {user_travel}")
#user_travel ← USER INPUT B

user_gas = float(input("\nHow much do you think you will spend on gas? "))
(f"Estimated Gas Expenses: ${user_gas:.2f}")
#user_gas ← USER INPUT C

user_hotel = float(input("\nApproximately, how much will you need for accommodation/hotel? "))
(f"Estimated Accommodation Expenses: ${user_hotel:.2f}")
#user_hotel ← USER INPUT D

user_food = float(input("\nLast, how much do you need for food? "))
(f"Estimated Food Expenses: ${user_food:.2f}\n")
# user_food ← USER INPUT E


print("------------- Travel Expenses -------------")
print(f"Location:          {user_travel}")
print(f"Initial Budget:    ${user_budget:.2f}")
print(f"Fuel:              ${user_gas:.2f}")
print(f"Accommodation:     ${user_hotel:.2f}")
print(f"Food:              ${user_food:.2f}")
print("-------------------------------------------") 

total_expenses = user_gas + user_hotel + user_food
remaining_balance = user_budget - total_expenses
print(f"Remaining Balance: ${remaining_balance:.2f}")
