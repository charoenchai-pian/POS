import pandas

class MenuMaker:

    def __init__(self):

        self.order_is_on = True
        self.value = 0
        self.price = ''

        # self.menu_list = ["thai", "italian", "japanese"]
    def choose_menu(self):
        self.menu = input("Which menu which you want to order? thai / italian / japanese?\n")
        if self.menu.lower() == "thai":
            self.data_menu = pandas.read_csv("Menu1_thai_food.csv")

        if self.menu.lower() == "japanese":
            self.data_menu = pandas.read_csv("Menu2_japanese_food.csv")

        if self.menu.lower() == "italian":
            self.data_menu = pandas.read_csv("Menu3_italian_food.csv")
        # for ct in self.menu_list:
        #     if self.menu == ct:
        #         self.data_menu = pandas.read_csv(f"Menu{}_{self.menu.lower()}_food.csv")

        self.food_list = self.data_menu["menu"].to_list()
        self.price_list = self.data_menu["price"].to_list()




    def choose_food(self):
        self.food = input(f"What would you like to order {self.food_list[0]}(${self.price_list[0]}), {self.food_list[1]}(${self.price_list[1]}), {self.food_list[2]}(${self.price_list[2]}) ?\n")
        for i in range(len(self.food_list)):
            if self.food_list[i] == self.food.lower():
                self.price = int(self.price_list[i])
        num = int(input("How many?\n"))
        self.price *= num
        self.value += self.price
        print(f"now = ${self.value}")


    def continue_order(self):
        answer = input(f"Any dish in {self.menu} y or n\n")
        if answer.lower() == 'y':
            self.choose_food()
            return True
        if answer.lower() == 'n':
            self.change_menu()
            return False

    def change_menu(self):
        answer = input("Change menu? y or n\n")
        if answer == 'y':
            self.choose_menu()
            self.choose_food()
        if answer == 'n':
            print("Thank you for coming")
            print(f"Total = {self.value}")
            self.order_is_on = False




