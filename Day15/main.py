# import data resources
from data import MENU, resources, profit

items = resources
required_resources = MENU


# 3. Print report.
def report(items):
    item_water = items["water"]
    item_milk = items["milk"]
    item_coffee = items["coffee"]
    money = profit

    print(f"Water: {item_water}ml \nMilk: {item_milk}ml \nCoffee: {item_coffee}g \nMoney: ${money}")


# 4. Check resources sufficient?
def check_resources(order_ingr):
    for item in order_ingr:
        if order_ingr[item] >= items[item]:
            print(f"Sorry there is not enough {item}")
            return False
        return True


def total_coins():
    print("Please insert coins.")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.10
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total


# 7. Make Coffee.
def make_coffee(order_ingr):
    for item in order_ingr:
        items[item] = items[item] - order_ingr[item]


# 1. Get user to provide an input
off = False
while not off:
    user_input = input("What would you like to drink? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
        report(items)
    elif user_input == "off":
        # 2. Turn off the Coffee Machine by entering off to the prompt.
        print("Powering off the Coffee Machine")
        off = True
    else:
        drink = MENU[user_input]
        if check_resources(drink["ingredients"]):
            total = total_coins()
            if total < MENU[user_input]["cost"]:
                print(f"Sorry that's not enough money. ${total} refunded.")
            else:
                profit += MENU[user_input]["cost"]
                change = total - MENU[user_input]["cost"]
                print(f"Here is ${round(change, 2)} in change.")
                make_coffee(drink["ingredients"])
                print("Here is your latte. Enjoy!")
