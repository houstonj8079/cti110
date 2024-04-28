# Jordan Houston-Taylor
# April 21, 2024
# P5LAB Assignment


# Define your function here.
def days_in_feb(user_year):
    if user_year % 4 == 0:
        if user_year % 100 == 0:
            if user_year % 400 == 0:
                return 29
            else:
                return 28
        else:
            return 29
    else:
        return 28
        
if __name__ == '__main__':
    year = int(input(""))
    print(f"{year} has {days_in_feb(year)} days in February.")

# Unit tests
def test_days_in_feb():
    assert days_in_feb(1913) == 28
    assert days_in_feb(1600) == 29
    assert days_in_feb(1900) == 28
