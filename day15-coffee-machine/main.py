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
    },
}

resources = {
    "water": 300,
    # "water": 0,
    "milk": 200,
    "coffee": 100,
    "profit": 0,
}


def get_order():
    return input("What would you like? (espresso/latte/cappuccino): ")


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Money: ${format(resources['profit'], '.2f')}")


def sufficient_resources(coffee):
    for coffee_ingredient in coffee["ingredients"]:
        if resources[coffee_ingredient] < coffee["ingredients"][coffee_ingredient]:
            print(f"Sorry there is not enough {coffee_ingredient}")
            return False

    return True


def brew_coffee(coffee, coffee_name):
    for coffee_ingredient in coffee["ingredients"]:
        resources[coffee_ingredient] -= coffee["ingredients"][coffee_ingredient]
    print(f"Here is your {coffee_name}. Enjoy!")


def handle_coins():
    total = 0
    coins = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01,
    }
    for coin in coins:
        total += float(input(f"How many {coin}? ")) * coins[coin]
    return round(total, 2)


def handle_transaction(payment, coffee):
    if payment >= coffee["cost"]:
        change = round(payment - coffee["cost"], 2)
        resources["profit"] += coffee["cost"]
        print(f"Here is ${change} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


machine_on = True

while machine_on:
    order = get_order().lower()
    if order == "off":
        machine_on = False
    elif order == "report":
        print_report()
    elif order in MENU and sufficient_resources(MENU[order]):
        print("Please insert coins.")
        payment = handle_coins()
        if handle_transaction(payment, MENU[order]):
            brew_coffee(MENU[order], order)
    elif order not in MENU:
        print("Sorry, invalid entry.")
        machine_on = False
