dict1 = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0
}


def print_report():
    for k, v in dict1.items():
        if k == "Water" or k == "Milk":
            print(f"{k}: {v}ml")
        elif k == "Coffee":
            print(f"{k}: {v}g")
        elif k == "Money":
            print(f"{k}: ${v}")


while True:
    q1 = input("What would you like? (espresso/latte/cappuccino): ")
    if q1 == "off":
        break
    if q1 == "report":
        print_report()
    if q1 == "espresso":
        if dict1["Water"] >= 50:
            if dict1["Coffee"] >= 18:
                q = int(input("Insert quarters: "))
                d = int(input("Insert dimes: "))
                n = int(input("Insert nickels: "))
                p = int(input("Insert pennies: "))
                total = q*.25 + d*.10 + n*.05 + p*.01
                if total >= 1.5:
                    dict1["Money"] += 1.5
                    dict1["Water"] -= 50
                    dict1["Coffee"] -= 18
                    print_report()
                    change = round(total - 1.5, 2)
                    if change > 0.0:
                        print(f"Here is ${change} dollars in change.")
                    else:
                        pass
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough water.")
    if q1 == "latte":
        if dict1["Water"] >= 200:
            if dict1["Coffee"] >= 24:
                if dict1["Milk"] >= 150:
                    q = int(input("Insert quarters: "))
                    d = int(input("Insert dimes: "))
                    n = int(input("Insert nickels: "))
                    p = int(input("Insert pennies: "))
                    total = q*.25 + d*.10 + n*.05 + p*.01
                    if total >= 2.5:
                        dict1["Money"] += 2.5
                        dict1["Water"] -= 200
                        dict1["Coffee"] -= 24
                        dict1["Milk"] -= 150
                        print_report()
                        change = round(total - 2.5, 2)
                        if change > 0.0:
                            print(f"Here is ${change} dollars in change.")
                        else:
                            pass
                    else:
                        print("Sorry that's not enough money. Money refunded.")
                else:
                    print("Sorry there is not enough Milk.")
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough water.")
    if q1 == "cappuccino":
        if dict1["Water"] >= 250:
            if dict1["Coffee"] >= 24:
                if dict1["Milk"] >= 100:
                    q = int(input("Insert quarters: "))
                    d = int(input("Insert dimes: "))
                    n = int(input("Insert nickels: "))
                    p = int(input("Insert pennies: "))
                    total = q*.25 + d*.10 + n*.05 + p*.01
                    if total >= 3.0:
                        dict1["Money"] += 3.0
                        dict1["Water"] -= 250
                        dict1["Coffee"] -= 24
                        dict1["Milk"] -= 100
                        print_report()
                        change = round(total - 3.0, 2)
                        if change > 0.0:
                            print(f"Here is ${change} dollars in change.")
                        else:
                            pass
                    else:
                        print("Sorry that's not enough money. Money refunded.")
                else:
                    print("Sorry there is not enough Milk.")
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough water.")
