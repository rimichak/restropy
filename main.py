#build a program where a user can view the menu select items and add multiple items to their order, calculate the final bill#
menus = {"Pizza": 150, "Burger": 200, "Biriyani": 250}

def view():
    count = 1
    print("========== Today's Menu ==========") 
    for item , price in menus.items():
        print(count, item, price)
        count += 1

def select_items():
   
   total = 0
   while True:
        selected_item = int(input("Select items from menus to orders: "))
        if selected_item == 1:
            print("you selected Pizza" )
            print("your bill is 150 RS")
            total += 150
        if selected_item == 2:
            print("you selected Burger" )
            print("your bill is 200 RS")
            total += 200
        if selected_item == 3:
            print("you selected Biriyani" )
            print("your bill is 250 RS")
            total += 250
        more = input("Want to add more items? Yes/No: ")

        if more == "No":
            break
   print("Total bill is: ", total)
   

view()
select_items()

