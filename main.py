# POS

from menu import MenuMaker
menu = MenuMaker()

menu.choose_menu()
menu.choose_food()
while menu.order_is_on:
    while menu.continue_order():
        continue
