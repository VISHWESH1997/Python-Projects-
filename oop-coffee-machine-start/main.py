from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

order = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
is_on = True
while is_on:
    item = input(f"What would you like? {order.get_items()}: ").lower()
    if item == "report":
        coffee.report()
        money.report()
    elif item == "off" :
        is_on = False
    else:
        drink = order.find_drink(item)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)






# print (drink)

#




