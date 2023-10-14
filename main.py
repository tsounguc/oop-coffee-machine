from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_options = Menu()
coffee_machine = CoffeeMaker()
cashier = MoneyMachine()


user_input = ""
while user_input.lower() != "off":
    user_input = input("What would you like? (" + menu_options.get_items() + "): ")
    if user_input == "report":
        coffee_machine.report()
        cashier.report()
    elif user_input.lower() == "espresso" or user_input.lower() == "latte" or user_input.lower() == "cappuccino":
        chosen_option = menu_options.find_drink(user_input)
        can_make_drink = coffee_machine.is_resource_sufficient(chosen_option)
        enough_money_given = cashier.make_payment(chosen_option.cost)
        if can_make_drink and enough_money_given:
            coffee_machine.make_coffee(chosen_option)