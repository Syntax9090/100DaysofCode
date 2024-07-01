# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    # The magic number 9/5
    # It's not a Harry Potter reference, I promise!
    magic_number = 9/5
    
    # The freezing point of water in Fahrenheit
    # Not the temperature of your ex's heart
    freezing_point = 32
    
    # Calculate Fahrenheit
    fahrenheit = (celsius * magic_number) + freezing_point
    
    return fahrenheit

# Take user input for Celsius
# No, we don't support input from the North Pole
celsius = float(input("Enter temperature in Celsius: "))

# Convert the input to Fahrenheit
# Abracadabra! The magic happens here.
fahrenheit = celsius_to_fahrenheit(celsius)

# Display the result
# Ta-da! Your temperature in Fahrenheit!
print(f"{celsius}°C is equal to {fahrenheit}°F")
