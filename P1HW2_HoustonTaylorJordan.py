# Jordan Houston-Taylor
# February 25, 2024
# P1HW2 Assignment
# The purpose of this project to create a python code that will be able to collect and process information.

print ("This program calculates and displays travel expenses")

user_budget = int(input("Enter budget integer:\n"))

print (f"Enter Budget: {user_budget}")

user_travel = int(input("Enter travel integer:\n"))

print (f"Enter your travel destination: {user_travel}")

user_gas = int(input("Enter gas integer:\n"))

print (f"How much do you think you will spend on gas? {user_gas}")

user_hotel = int(input("Enter hotel integer:\n"))

print (f"Approximately, how much will you need for accomodation/hotel? {user_hotel}")

user_food = int(input("Enter food integer:\n"))

print (f"Last, how much do you need for food? {user_food}")


print("------------- Travel Expenses -------------")

print (f"Location: {user_travel}")
print (f"Initial Budget: {user_budget}")

print (f"Fuel: {user_gas}")
print (f"Accomodation: {user_hotel}")
print (f"Food: {user_food}")


balance = user_budget - user_gas - user_hotel - user_food


print (f"Remaining Balance: {balance}")
