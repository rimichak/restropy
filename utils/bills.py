import os

def save_bill(cart, total):
    folder = "bills"

    if not os.path.exists(folder):
        os.makedirs(folder)
    file_path = os.path.join(folder, "bill.txt")

    with open(file_path, "w") as file:
         file.write("===== FOOD BILL =====\n\n")

         for item, price in cart:
            file.write(f"{item} ₹{price}\n")

            file.write("\n----------------------\n")
    file.write(f"Total: ₹{total}\n")

    print(f"✅ Bill saved in {file_path}")