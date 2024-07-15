from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
cash_register = MoneyMachine()

espresso = MenuItem("espresso", 50, 0, 18, 1.5)
latte = MenuItem("latte", 200, 150, 24, 2.5)
cappucino = MenuItem("cappucino", 250, 100, 24, 3.0)

get_more_coffee = True
quitting = False

order = ""


def take_order():
    continue_ordering = True

    while continue_ordering:
        order = input(f"What would you like? ({coffee_menu.get_items()}) ")

        if order == "report":
            coffee_maker.report()
        elif order == "quit":
            return False
        else:
            return coffee_menu.find_drink(order)


order = take_order()

while get_more_coffee:

    if not order:
        break

    if coffee_maker.is_resource_sufficient(order) and cash_register.make_payment(order.cost):
        coffee_maker.make_coffee(order)
    else:
        print("Couldn't make the coffee!")

    order = take_order()
