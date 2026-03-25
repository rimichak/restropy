#build a program where a user can view the menu select items and add multiple items to their order, calculate the final bill#
from utils.bills import save_bill

menus = {"Pizza": 150, "Burger": 200, "Biriyani": 250}

def view():
    count = 1
    print("========== Today's Menu ==========") 
    for item , price in menus.items():
        print(count, item, price)
        count += 1

def select_items():
   
   cart = []
   total = 0
   while True:
        try:
            selected_item = int(input("Select items from menus to orders: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        if selected_item == 1:
            item = "Pizza"
            price = menus[item]
            cart.append((item, price))
            print("you selected Pizza" )
            print(f"your bill is {price} RS")
            total += price
        if selected_item == 2:
            item = "Burger"
            price = menus[item]
            cart.append((item, price))
            print("you selected Burger" )
            print(f"your bill is {price} RS")
            total += price
        if selected_item == 3:
            item = "Biriyani"
            price = menus[item]
            cart.append((item, price))
            print("you selected Biriyani" )
            print(f"your bill is {price} RS")
            total += price

        while True:
            more = input("Want to add more items? Yes/No: ").strip().lower()

            if more in ["yes", "y"]:
                break  

            elif more in ["no", "n"]:
                break 

            else:
                print("Invalid input! Please type Yes/Y or No/N.")
        if more in ["no", "n"]:    
            break

   print(" ---- Order Summary ---- ")
   print("--- Item Ordered ----")

   if not cart:
       print("no item is ordered.")
   else:

       for item , price in cart:
            print(f"{item} - {price} /-")

       print(f"Total bill is: {total} /-")
       save_bill(cart, total)
   

view()
select_items()

