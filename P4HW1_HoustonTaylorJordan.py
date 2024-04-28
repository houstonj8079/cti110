# Jordan Houston-Taylor
# April 14, 2024
# P4HW1 Assignment
# This will help me build on upon a previous assignment with the use of loop commands.

def calculate_grade(average_score):
    if average_score >= 90:
        return "A"
    elif average_score >= 80:
        return "B"
    elif average_score >= 70:
       return "C"
    elif average_score >= 60:
        return "D"
    else:
        return "F"

def main():
    num_scores = int(input("How many scores do you want to enter? "))
    score_list = []
    
    # Collect scores
    count = 1
    while count <= num_scores:
        score = int(input(f"Enter score #{count}: "))
        if score >= 0 and score <= 100:
            score_list.append(score)
            count += 1
        else:
            print("INVALID Score entered!!!!")
            print("Score must be between 0 and 100.")
            score = int(input(f"Enter score #{count} again: "))
            if score >= 0 and score <= 100:
                score_list.append(score)
                count += 1

    print("--------------------Results--------------------")

    # Find lowest score
    lowest_score = min(score_list)
    print(f"Lowest score : {lowest_score}")

    # Remove lowest score
    score_list.remove(lowest_score)

    # Format the score_list with decimal points
    format_list = [f"{score:.1f}" for score in score_list]

    # Calculate average score
    average_score = sum(score_list) / len(score_list)
    print(f"Modified List : {format_list}")
    print(f"Scores Average: {average_score:.2f}")

    # Determine letter grade
    grade = calculate_grade(average_score)
    print(f"Grade: {grade}")

    print("-----------------------------------------------")

    
if __name__ == "__main__":
    main()
