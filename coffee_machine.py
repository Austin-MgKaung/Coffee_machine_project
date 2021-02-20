class coffee_machine:

    def __init__(self):
        self.t_water = 400
        self.t_milk = 540
        self.t_coffee = 120
        self.t_cup = 9
        self.t_money = 550



    def espresso(self):
        # global t_water, t_coffee, t_money, t_cup
        self.t_water -= 250
        self.t_coffee -= 16
        self.t_money += 4
        self.t_cup -= 1

        if self.is_enough():
            print("I have enough resources, making you a coffee!")
        else:
            self.t_water += 250
            self.t_coffee += 16
            self.t_money -= 4
            self.t_cup += 1

    def latte(self):
        # global t_water, t_coffee, t_milk, t_money, t_cup
        self.t_water -= 350
        self.t_coffee -= 20
        self.t_milk -= 75
        self.t_money += 7
        self.t_cup -= 1

        if self.is_enough():
            print("I have enough resources, making you a coffee!")
        else:
            self.t_water += 350
            self.t_coffee += 20
            self.t_milk += 75
            self.t_money -= 7
            self.t_cup += 1

    def cappuccino(self):
        # global t_water, t_coffee, t_milk, t_money, t_cup
        self.t_water -= 200
        self.t_coffee -= 12
        self.t_milk -= 100
        self.t_money += 6
        self.t_cup -= 1

        if self.is_enough():
            print("I have enough resources, making you a coffee!")
        else:
            self.t_water += 200
            self.t_coffee += 12
            self.t_milk += 100
            self.t_money -= 6
            self.t_cup += 1

    def print_menu(self):
        print(f"""The coffee machine has:
                   {self.t_water} of water
                   {self.t_milk} of milk
                   {self.t_coffee} of coffee beans
                   {self.t_cup} of disposable cups
                   ${self.t_money} of money\n""")

    def take(self):
        # global t_money
        take_money = self.t_money
        print(f"I gave you ${take_money}")
        self.t_money = 0
        return take_money

    def fill(self):
        # global t_water, t_milk, t_coffee, t_cup
        f_water = int(input("Write how many ml of water do you want to add:\n"))
        f_milk = int(input("Write how many ml of milk do you want to add:\n"))
        f_coffee = int(input("Write how many grams of coffee beans do you want to add:\n"))
        f_cup = int(input("Write how many disposable cups of coffee do you want to add:\n"))
        self.t_water += f_water
        self.t_milk += f_milk
        self.t_coffee += f_coffee
        self.t_cup += f_cup

    def buy(self):
        # global t_cup
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
        # t_cup -= 1
        if coffee_type == "1":
            self.espresso()
        elif coffee_type == "2":
            self.latte()
        elif coffee_type == "3":
            self.cappuccino()
        elif coffee_type == "back":
            pass
        else:
            pass

    def is_enough(self):
        if self.t_water < 0:
            print("Sorry, not enough water!")
            return False
        elif self.t_milk < 0:
            print("Sorry, not enough milk!")
            return False
        elif self.t_coffee < 0:
            print("Sorry, not enough coffee bean!")
            return False
        elif self.t_cup < 0:
            print("Sorry, not enough cup!")
            return False
        else:
            return True

    def take_action(self, _action):
        if _action.lower() == "take":
            self.take()
            return True
        elif _action.lower() == "buy":
            self.buy()
            return True
        elif _action.lower() == "fill":
            self.fill()
            return True
        elif _action.lower() == "remaining":
            self.print_menu()
            return True
        elif _action.lower() == "exit":
            return False
        else :
            return True


def main():
    end_trigger = True
    mycoffee_machine = coffee_machine()
    while end_trigger:
        action = input("Write action (buy, fill, take, remaining, exit):\n")
        end_trigger = mycoffee_machine.take_action(action)

if __name__ == "__main__":
    main()