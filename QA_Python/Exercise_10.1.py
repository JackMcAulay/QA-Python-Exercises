price = {"Burger": 5.55, "Hotdog":5.25}

user_funds = 0
item_price = price["Burger"]

if item_price < user_funds:
    print("You have enough money!")
elif item_price == user_funds:
    print("You have the precise amount of money")
else:
    print("Sorry you don't have enough money")