print("Welcome to the tip calculator!")

# Get the total bill amount (time to face the truth!)
bill = float(input("What was the total bill? $"))

# Get the tip percentage (let's be generous, or not!)
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

# Get the number of people to split the bill (the more, the merrier!)
people = int(input("How many people to split the bill?"))

# Calculate the tip as a percentage (math is hard, but we got this)
tip_as_percent = tip / 100

# Calculate the total tip amount (hope you brought your wallet)
total_tip_amount = bill * tip_as_percent

# Calculate the total bill including the tip (ouch, that hurts)
total_bill = bill + total_tip_amount

# Calculate the amount each person should pay (sharing is caring)
bill_per_person = total_bill / people

# Round the final amount to 2 decimal places (because nobody likes pennies)
final_amount = round(bill_per_person, 2)

# Print the final amount each person should pay (don't cry, it'll be okay)
print(f"Each person should pay: ${final_amount}")
