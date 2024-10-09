menu_categories = ["Appetizer",
                   "Main Course",
                   "Drinks",
                   "Desserts"]
# Accessing Menu
menu_items = [
    ['Garlic Bread Stick', 'Deviled Eggs', 'Soup', 'Salad'],
    ['Adobo', 'Potato Gnocchi', 'T bone steak & mashed potato', 'Roasted Salmon', 'Grilled Scallops with Cream corn',
     'Grilled Garlic and pepper shrimp'],

        ['Coconut Juice', 'watermelon Shake', 'Ice tea', 'Lemonade'],
    ['Mango Ice Cream', 'Chocolate Muffins', 'Halo Halo', 'Lemon Tarts']
]
# Accessing Price
menu_prices = [
    [45, 135, 80, 150],
    [200, 175, 620, 450, 545, 450],
    [80, 50, 80, 60],
    [75, 95, 60, 70]
]
currentOrder = []
# to be used on sales summary
completed_orders = []
total_earnings = []

def view_menu():
    print("\n ==== Menu ==== ")

    # display all categories
    for i in range(len(menu_categories)):
        print(f"{menu_categories[i]}:")
        # display all items in each category
        for j in range(len(menu_items[i])):
            print(f"\t{j + 1}. {menu_items[i][j].ljust(40)} - ₱{menu_prices[i][j]:>6.2f}")

    print("\n1. Return to the Main Menu")
    print("2. Proceed with an order")

def add_item():

    # User input, error handling
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

    # if category selected is within the index boundary, proceed
    if 0 <= category_index < 4:
        for j in range(len(menu_items[category_index])):
            print(f"{j + 1}. {menu_items[category_index][j].ljust(35)} ${menu_prices[category_index][j]:>6.2f}")

        # Validation of item selected
        while True:
            item = input("Please select an item: ")
            if item.isdigit():
                item_index = int(item) - 1
                break
            elif item == "r":
                return
            else:
                print("\nPlease enter a valid item.")

        # Validation of Quantity
        while True:

            quantity_input = input("Please select a quantity: ")

            if quantity_input.isdigit():
                quantity = int(quantity_input)
                break

            else:
                print("\nPlease enter a valid quantity.")

        # Check if item selected is within the boundary of choices
        if 0 <= item_index < len(menu_items[category_index]):
            currentOrder.append([category_index, item_index, quantity])
            print(f"Your order has been placed")


def remove_item():

    # if not empty
    if not currentOrder:
        return False

    for i in range(len(currentOrder)):
        category, item, qauntity = currentOrder[i]
        # Displaying all orders in the order they were purchased.
        print(f"{i + 1}. {menu_items[category][item]} - {qauntity}x ${menu_prices[category][item]:}")

    # Validation of Input
    while True:
        item_to_remove = input("Please select an item to remove: ")
        if item_to_remove.isdigit():
            item_to_remove_index = int(item_to_remove) - 1
            break
        elif item_to_remove == "r":
            return
        else:
            print("\nPlease enter a valid item.")

    # Boundary of input validation
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

    # total amount of payment from review_order function
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

    tax = totalPrice * 0.15
    total_with_tax = totalPrice + tax
    print(f"\t Tax (15%): ${tax:,.2f}")
    print(f"\t Total Price with Tax: ${total_with_tax:,.2f}")

    while True:
        amount_input = input("Please enter your payment amount: ")

        if amount_input.isdigit():
            payment_amount = int(amount_input)

            if payment_amount >= total_with_tax:
                print(f"Amount Due: ${payment_amount - total_with_tax:,.2f}")

                for order in currentOrder:
                    completed_orders.append(order)
                total_earnings.append(total_with_tax)
                break

            elif payment_amount < total_with_tax:
                print(f"\tInsufficient funds")
                print(f"\tPlease try again")

            else:
                print("Thank You")

        else:
            print("Invalid input")

    #transaction complete, clear the current order list for new transaction
    currentOrder.clear()
    return True

def view_sales_summary():

    # Check if completed order is empty
    if not completed_orders:
        print("No completed orders")
        return
    
    revenue = 0

    for order in completed_orders:
        category, item, quantity = order
        print(f"{menu_items[category][item]}, {quantity}")
    for earnings in total_earnings:
        revenue += earnings
    print(revenue)

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
                # Reviewing order
                if review_order():
                    # if user have current orders
                    while True:
                        print("1. Remove an item")
                        print("2. Proceed to payment")
                        print("3. Return")
                        sub_choice = input("Please Select an option: ")
                        if sub_choice == "1":
                            remove_item()
                        elif sub_choice == "2":
                            if payment():
                                currentOrder.clear()
                                return
                        elif sub_choice == "3":
                            break
                else:
                    print("No current orders")
            case "3":
                while True:
                    make_sure = input("Are you sure you would like to cancel the order? yes/no: ").lower()
                    if make_sure == "yes":
                        currentOrder.clear()
                        return
                    else:
                        break
            case _:
                print("Invalid Selection, please try again.")

def main():

    while True:
        print("== Main Menu ==")
        print("1. View Menu")
        print("2. View Sales Summary | Not Available")
        print("3. Place Order")
        print("4. Exit")

        choice = input("Select an option: ")
        print()

        if choice == "1":
            view_menu()
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


if __name__ == "__main__":
    main()
