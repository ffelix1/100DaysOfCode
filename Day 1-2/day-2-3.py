# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
age = int(age)
yearsRemaining = 90 - age
daysRemaining = yearsRemaining * 365
weeksRemaining = yearsRemaining * 52
monthsRemaining = yearsRemaining * 12
#print(monthsRemaining)
print(f"you have {daysRemaining} days, {weeksRemaining} weeks, and {monthsRemaining} months left ")
