# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆
BMI = round(height / weight ** 2)
# BMI = round( weight / (height **2) * 703)
# Write your code below this line 👇
if BMI < 18.5:
    print(f"Your BMI is {BMI}, which you are under weight")
elif BMI < 25:
    print(f"Your BMI is {BMI}, which you are normal weight")
elif BMI < 30:
    print(f"Your BMI is {BMI}, which you are slightly overweight")
elif BMI < 35:
    print(f"Your BMI is {BMI}, which you are obese")
else:
    print(f"You BMI is {BMI}, which you are clinically obese")
