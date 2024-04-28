#Jordan Houston-Taylor

#April 28, 2024

#P5HW Assignment 

#This assignment will help me create a math quiz using loops.



print("Welcome to Math Quiz\n")

import random

def generate_numbers():
    """Generate two random numbers between 1 and 100."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

def addition_quiz():
    """Generate numbers, ask for the sum, and display results."""
    num1, num2 = generate_numbers()
    correct_answer = num1 + num2
    guesses = 0

    print(f"\n{num1} \n+ {num2}")

    while True:
        try:
            user_answer = int(input("\nEnter answer: "))
            guesses += 1
            
            if user_answer == correct_answer:
                print(f"Congratulations!!!! Your answer is correct. \nNumber of guesses: {guesses}")
                break
            elif user_answer < correct_answer:
                print("Sorry, guess is too low.")
            else:
                print("Sorry, guess is too high.")
        except ValueError:
                print("Please enter a valid integer.")
            

def subtraction_quiz():
    """Generate numbers, ask for the difference, and display results."""
    num1, num2 = generate_numbers()
    correct_answer = num1 - num2
    guesses = 0

    print(f"\n{num1} \n- {num2}")

    while True:
        try:
            user_answer = int(input("\nEnter your answer: "))
            guesses += 1
            
            if user_answer == correct_answer:
                print(f"Congratulations!!!! Your answer is correct. \nNumber of guesses: {guesses}")
                break
            elif user_answer < correct_answer:
                print("Sorry, guess is too low.")
            else:
                print("Sorry, guess is too high.")
        except ValueError:
                print("Please enter a valid integer.")
            

def main():
    while True:
        print("\nMAIN MENU \n---------------------")
        print("1. Adding Random Numbers")
        print("2. Subtraction Random Numbers")
        print("3. Exit\n")
        
        choice = input("Please choose one of the menu options: ")

        if choice == '1':
            addition_quiz()
        elif choice == '2':
            subtraction_quiz()
        elif choice == '3':
            print("Thank you for playing... \nBye!!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
