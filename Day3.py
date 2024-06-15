#Usuing Control conditional statements 
#BMI
# Enter your height in meters e.g., 1.55
height = float(input())

# Enter your weight in kilograms e.g., 72
weight = int(input())

# 🚨 Don't change the code above 👆

# Calculate BMI using the formula: weight divided by height squared
BMI = weight / (height * height)

# Print the calculated BMI
print(BMI)

# Determine the BMI category and print the corresponding message
if BMI < 18.5:
    # If BMI is less than 18.5, the person is underweight
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    # If BMI is between 18.5 and 24.9, the person has a normal weight
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
    # If BMI is between 25 and 29.9, the person is slightly overweight
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    # If BMI is between 30 and 34.9, the person is obese
    print(f"Your BMI is {BMI}, you are obese.")
else:
    # If BMI is 35 or more, the person is clinically obese
    print(f"Your BMI is {BMI}, you are clinically obese.")
