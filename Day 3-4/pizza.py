# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
print("Small Pizza: $15\n" + " Medium Pizza: $20\n" + " Large Pizza: $25\n")
print(
    f"Pepperoni for Small Pizza: +$2\n" + "Pepperoni for Medium or Large Pizza: +$3\n" + "Extra cheese for any size pizza: + $1\n")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"The total is {bill}")
