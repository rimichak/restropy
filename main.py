#build a program where a user can view the menu select items and add multiple items to tehir order, calculate the final bill#
menus = {"Pizza": 150, "Burger": 200, "Biriyani": 250}

def view():
    count = 1
    print("========== Today's Menu ==========") 
    for item , price in menus.items():
        print(count, item, price)
        count += 1

def select_items():

   selected_item = int(input("Select items from menus to orders: "))
   if selected_item == 1:
       print("you selected Pizza" )
       print("your bill is 150 RS")
   if selected_item == 2:
       print("you selected Burger" )
       print("your bill is 200 RS")
   if selected_item == 3:
       print("you selected Biriyani" )
       print("your bill is 250 RS")



view()
select_items()

