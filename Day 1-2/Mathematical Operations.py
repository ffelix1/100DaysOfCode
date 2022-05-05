# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmiCalculation = int(weight) / float(height) ** 2
bmi = round(bmiCalculation, 2)  # the comma is the number to given to decimal digits 2.22 if it's (3/3,2)
# print( bmi)
print(f"This is your BMI {bmi}") #add f in front of a string and you can add the other variables that aren't string in your statement

print(8 // 3)  # is automatic float and its easier to use this than using the word float in front of it
score = 0
score += 1
print(score)
