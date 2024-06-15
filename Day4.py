# Prompt the user to enter the year to check
year = int(input("Which year do you want to check? "))

# Check if the year is divisible by 4
if year % 4 == 0:
    # If the year is divisible by 4, check if it is also divisible by 100
    if year % 100 == 0:
        # If the year is divisible by 100, check if it is also divisible by 400
        if year % 400 == 0:
            # If the year is divisible by 400, it is a leap year
            print("Leap year.")
        else:
            # If the year is divisible by 100 but not by 400, it is not a leap year
            print("Not leap year.")
    else:
        # If the year is divisible by 4 but not by 100, it is a leap year
        print("Leap year.")
else:
    # If the year is not divisible by 4, it is not a leap year
    print("Not leap year.")
