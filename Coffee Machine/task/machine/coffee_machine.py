class CoffeeMachine:
    prompt_message = {
        "Ready": "\nWrite action (buy, fill, take, remaining, exit): ",
        "buy": "\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ",
        "water": "\nWrite how many ml of water do you want to add: ",
        "milk": "Write how many ml of milk do you want to add: ",
        "beans": "Write how many grams of coffee beans do you want to add: ",
        "cups": "Write how many disposable cups of coffee do you want to add: "
    }

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = "Ready"

    def __str__(self):
        levels = f"\nThe coffee machine has:\n{self.water} of water\n{self.milk} of milk\n"
        levels += f"{self.beans} of coffee beans\n{self.cups} of disposable cups\n{self.money} of money"
        return levels

    def check_levels(self, ammounts):
        make_coffee = False
        if ammounts["water"] > self.water:
            print("Sorry, not enough water!")
        elif ammounts["milk"] > self.milk:
            print("Sorry, not enough milk!")
        elif ammounts["beans"] > self.beans:
            print("Sorry, not enough coffee beans!")
        elif self.cups == 0:
            print("Sorry, not enough disposable cups!")
        else:
            make_coffee = True
            print("I have enough resources, making you a coffee!")
        return make_coffee

    def buy(self, drink):
        self.state = "Ready"
        change_levels = {
            '1': {"water": 250, "milk": 0, "beans": 16, "money": 4},
            '2': {"water": 350, "milk": 75, "beans": 20, "money": 7},
            '3': {"water": 200, "milk": 100, "beans": 12, "money": 6}
        }
        if drink in change_levels:
            change = change_levels[drink]
        else:
            print("Invalid selection")
            self.state = "buy"
            return

        if self.check_levels(change):
            self.water -= change["water"]
            self.milk -= change["milk"]
            self.beans -= change["beans"]
            self.cups -= 1
            self.money += change["money"]

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def get_state(self):
        print(CoffeeMachine.prompt_message[self.state])
        new_state = input()
        if self.state == "buy":
            if new_state == "back":
                self.state = "Ready"
            else:
                self.buy(new_state)
        elif self.state == "water":
            self.state = "milk"
            self.water += int(new_state)
        elif self.state == "milk":
            self.state = "beans"
            self.milk += int(new_state)
        elif self.state == "beans":
            self.state = "cups"
            self.beans += int(new_state)
        elif self.state == "cups":
            self.state = "Ready"
            self.cups += int(new_state)
        elif new_state == "fill":
            self.state = "water"
        elif new_state == "take":
            self.take()
        elif new_state == "remaining":
            print(self)
        elif new_state == "exit":
            self.state = "exit"
        else:
            self.state = "buy"


machine = CoffeeMachine()
while machine.state != "exit":
    machine.get_state()
