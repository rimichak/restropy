#build a program where a user can view the menu select items and add multiple items to tehir order, calculate the final bill#
menus = {"Pizza": 150, "Burger": 200, "Biriyani": 250}

def view():
    count = 1
    print("*** Today's Menu ***") 
    for item , price in menus.items():
        print(count, item, price)
        count += 1

def select_items():
    pass


view()

