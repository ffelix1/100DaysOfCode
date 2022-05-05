heightNumber = int(input("What is your height in cm?"))
if heightNumber >= 120:
    age= int(input("How old you?"))
    if age < 12:
        print("it's going to be 5 bucks")
    elif age <= 18: #
         print("it's 7 bucks")
    else:
        print("it's 12 bucks")
else:
    print("you are too small to go in")