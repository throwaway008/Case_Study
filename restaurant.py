menu_categories = ["Appetizer",
                   "Main Course",
                   "Drinks",
                   "Desserts"]

menu_items = [
    ['Garlic Bread Stick', 'Deviled Eggs', 'Soup', 'Salad'],
    ['Adobo', 'Potato Gnocchi', 'T bone steak & mashed potato', 'Roasted Salmon', 'Grilled Scallops with Cream corn',
     'Grilled Garlic and pepper shrimp'],

    ['Mango Ice Cream', 'Chocolate Muffins', 'Halo Halo', 'Lemon Tarts'],
    ['Coconut Juice', 'watermelon Shake', 'Ice tea', 'Lemonade']
]

menu_prices = [
    [45, 135, 80, 150],
    [200, 175, 620, 450, 545, 450],
    [80, 50, 80, 60],
    [75, 95, 60, 70]
]

currentOrder = []

completed_orders = []


def view_menu():
    print("\n ==== Menu ==== ")

    for i in range(len(menu_categories)):
        print(f"{menu_categories[i]}:")
        # i = 0
        for j in range(len(menu_items[i])):
            print(f"\t{j + 1}. {menu_items[i][j].ljust(40)} - ₱{menu_prices[i][j]:>6.2f}")  # I don't know

    print("\n1. Return to the Main Menu")
    print("2. Proceed with an order")


def add_item():
    while True:
        print("Please choose a category to add items from: ")
        for i in range(len(menu_categories)):
            print(f"{i + 1}. {menu_categories[i]}")

        category = input("\nPlease choose a category or enter 'r' to return: ")

        if category.isdigit():
            category_index = int(category) - 1
            break

        elif category == "r":
            return

        else:
            print("\nPlease enter a valid category.")

    if 0 <= category_index < 4:
        for j in range(len(menu_items[category_index])):
            print(f"{j + 1}. {menu_items[category_index][j].ljust(35)} ${menu_prices[category_index][j]:>6.2f}")

        # Validation item selection
        while True:

            item = input("Please select an item: ")

            if item.isdigit():
                item_index = int(item) - 1
                break

            elif item == "r":
                return

            else:
                print("\nPlease enter a valid item.")

        # Quantity
        while True:

            quantity_input = input("Please select a quantity: ")

            if quantity_input.isdigit():
                quantity = int(quantity_input)
                break

            else:
                print("\nPlease enter a valid quantity.")

        if 0 <= item_index < len(menu_items[category_index]):
            currentOrder.append([category_index, item_index, quantity])
            print(f"Your order has been placed")


def remove_item():

    if not currentOrder:
        return False

    for i in range(len(currentOrder)):
        category, item, qauntity = currentOrder[i]

        print(f"{i + 1}. {menu_items[category][item]} - {qauntity}x ${menu_prices[category][item]:}")

    while True:

        item_to_remove = input("Please select an item to remove: ")

        if item_to_remove.isdigit():
            item_to_remove_index = int(item_to_remove) - 1
            break

        elif item_to_remove == "r":
            return

        else:
            print("\nPlease enter a valid item.")

    if 0 <= item_to_remove_index < len(currentOrder):
        currentOrder.pop(item_to_remove_index)
        print(f"Your order has been removed")
        for i in range(len(currentOrder)):
            category, item, quantity = currentOrder[i]

            print(f" {menu_items[category][item]} - {quantity}x ${menu_prices[category][item]}")

def review_order():

    totalPrice = 0

    if currentOrder:

        print("---------------------------------")
        for order in currentOrder:
            category, item, quantity = order
            price = menu_prices[category][item]

            totalPrice += price * quantity
            print(f"\t({quantity}x) {menu_items[category][item].ljust(40)} - ${menu_prices[category][item] * quantity:>6.2f}")
        print("---------------------------------")

        print(f"Sales: ${totalPrice}\n")

        return totalPrice

def payment():


    if not currentOrder:
        return

    totalPrice = review_order()



    # Error Handling
    while True:
        discount = input("Are you qualified for discount | (PWD/Senior): Y/N").lower()

        if discount == "y":
            totalPrice = totalPrice * 0.80
            print(f"Discount: {totalPrice * 0.20}")
            break

        elif discount == "n":
            break

        else: print("Invalid Selection")

    print(f"\t Tax (15%): ${totalPrice * 0.15:,.2f}")
    print(f"\t Total Price with Tax: ${totalPrice + (totalPrice * 0.15):,.2f}")

    while True:
        amount_input = input("Please enter your payment amount: ")

        if amount_input.isdigit():
            payment_amount = int(amount_input)

        else:
            print("Invalid input")


        if payment_amount > totalPrice:
            print(f"Amount Due: ${payment_amount - totalPrice:,.2f}")

            for order in currentOrder:
                completed_orders.append(order)

            return True


        elif payment_amount < totalPrice:
            print(f"\tInsufficient funds")
            print(f"\tPlease try again")

        else:
            print("Thank You")





def view_sales_summary():

    # Check if completed order is empty
    if not completed_orders:
        print("No completed orders")
        return

    # category, item, quantity

    for order in completed_orders:
        category, item, quantity = order

        print(f"{menu_categories[category][item]} - ${menu_prices[category][item]}")


def place_order():

    while True:
        print("\nPlace Order Menu:")
        print("1. Add an item")
        print("2. Review Order")
        print("3. Cancel order and return to main menu")

        order_choice = input("Select an option: ")

        match order_choice:
            case "1":
                add_item()
            case "2":
                if review_order():
                    while True:
                        print("1. Remove an item")
                        print("2. Proceed to payment")
                        print("3. Return")
                        sub_choice = input("Please Select an option: ")

                        if sub_choice == "1":
                            remove_item()
                        elif sub_choice == "2":
                            if payment():
                                print("Here")
                                return
                        elif sub_choice == "3":
                            break
                else:
                    print("-------------------------------")
            case "3":
                while True:
                    make_sure = input("Are you sure you would like to cancel the order? yes/no").lower()
                    if make_sure == "yes":
                        currentOrder = []
                        return
            case _:
                print("Invalid Selection, please try again.")

    # clear orders on choice 5

    # use while loop for error handling


def main():

    while True:
        print("== Main Menu ==")
        print("1. View Menu")
        print("2. View Sales Summary")
        print("3. Place Order")
        print("4. Exit")

        choice = input("Select an option: ")
        print()

        if choice == "1":
            view_menu()

            # Error Handling
            submenu_choice = input("Select an option: ")

            if submenu_choice == "2":
                place_order()



            else:
                print("--> Invalid Input | Please select again <--")

        elif choice == "2":
            view_sales_summary()

        elif choice == "3":
            place_order()

        elif choice == "4":
            print("Program Terminated!!!")
            return

        else:
            print("--> Invalid Selection <--")

    # only choice 1 habe a submenu option -> Proceed taking orders


if __name__ == "__main__":
    main()
