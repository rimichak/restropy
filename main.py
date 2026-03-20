#build a program where a user can view the menu select items and add multiple items to their order, calculate the final bill#
menus = {"Pizza": 150, "Burger": 200, "Biriyani": 250}

def view():
    count = 1
    print("========== Today's Menu ==========") 
    for item , price in menus.items():
        print(count, item, price)
        count += 1

def select_items():
   
<<<<<<< HEAD
   cart = []
=======
>>>>>>> 59f0cbf015bc6bff4f9f2cf2e803735f9ca7aa0f
   total = 0
   while True:
        selected_item = int(input("Select items from menus to orders: "))
        if selected_item == 1:
<<<<<<< HEAD
            cart.append(("Pizza", 150))
=======
>>>>>>> 59f0cbf015bc6bff4f9f2cf2e803735f9ca7aa0f
            print("you selected Pizza" )
            print("your bill is 150 RS")
            total += 150
        if selected_item == 2:
<<<<<<< HEAD
            cart.append(("Burger", 200))
=======
>>>>>>> 59f0cbf015bc6bff4f9f2cf2e803735f9ca7aa0f
            print("you selected Burger" )
            print("your bill is 200 RS")
            total += 200
        if selected_item == 3:
<<<<<<< HEAD
            cart.append(("Biriyani", 250))
            print("you selected Biriyani" )
            print("your bill is 250 RS")
            total += 250

        more = input("Want to add more items? Yes/No: ")

        if more == "No":
            break

   print(" ---- Order Summary ---- ")
   print("--- Item Ordered ----")

   for item , price in cart:
       print(f"{item} - {price} /-")
   print(f"Total bill is: {total} /-")

=======
            print("you selected Biriyani" )
            print("your bill is 250 RS")
            total += 250
        more = input("Want to add more items? Yes/No: ")

        if more == "No":
            break
   print("Total bill is: ", total)
   
>>>>>>> 59f0cbf015bc6bff4f9f2cf2e803735f9ca7aa0f

view()
select_items()

