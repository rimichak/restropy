from menus.menu import menus

def view():
    count = 1
    print("========== Today's Menu ==========") 
    for item , price in menus.items():
        print(count, item, price)
        count += 1