heightNumber = int(input("What is your height in cm?"))
bill = 0

if heightNumber >= 120:
    age = int(input("How old you?"))
    if age < 12:
        bill = 5
        print("it's going to be 5 bucks")
    elif age <= 18:
        bill = 7
        print("it's 7 bucks")
    elif age >= 45 and age <= 55:
        bill = 0
        print("it's free")
    else:
        bill = 12
        print("it's 12 bucks")
    wantPhoto = input("Do you want a photo taken? yes or no. ")
    if wantPhoto == "yes" or "y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("you are too small to go in")
