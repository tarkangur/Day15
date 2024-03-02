MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def check_rss(drink, resources):
    for i in drink["ingredients"]:
        if drink["ingredients"][i] >= resources[i]:
            print(f"Sorry there is not enough {i}")
            return False
        else:
            return True

def check_money(quarters, dimes, nickles,pennies):

    return quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01


money = 0
choice = ""
while choice != "off":
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "report":
        print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${money:.2f}")

    elif choice == "off":
        exit()

    else:
        drink = MENU[choice]
        check = check_rss(drink, resources)
        while check:
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            insert_coin = check_money(quarters, dimes, nickles, pennies)

            if insert_coin < drink["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = insert_coin-drink["cost"]
                print(f"Here is ${change:.2f} in change.")
                print(f"Here is your {choice} ☕️. Enjoy!")
                money += insert_coin - change
                for i in drink["ingredients"]:
                    resources[i] -= drink["ingredients"][i]
            break





