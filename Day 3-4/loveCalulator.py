# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lowerName = name1.lower()
countName = lowerName.count()

lowerName2 = name2.lower()
countName2 = lowerName2.count()
loveScore= 0
if loveScore >= 10 or loveScore <=90:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif 40 >= loveScore >= 50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")