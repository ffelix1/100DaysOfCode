# 1. Create a greeting for your program.
print("Welcome to the first name branding generator")
# 2. Ask the user for the city that they grew up in.
cityName = input("What city did you grow up?\n")
# 3. Ask the user for the name of a pet.
petName = input("What is your name of your pet?\n")

# 4. Combine the name of their city and pet and show them their band name.
print(f"Sweet! So the city is {cityName} and your pet's name is {petName}\n")
bandName = cityName + " " + petName
print("So your band must be something like " + bandName)
# 5. Make sure the input cursor shows on a new line, see the example at:
