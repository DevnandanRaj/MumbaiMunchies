inventory = {}
sales = []

def add_item(id, name, price, availability, quantity):
    item = {
        "name": name,
        "price": price,
        "availability": availability,
        "quantity": quantity
    }
    inventory[id] = item
    print(f"Item with ID {id} has been added to the inventory.")

def remove_item(id):
    if id in inventory:
        del inventory[id]
        print(f"Item with id {id} has been removed.")
    else:
        print(f"Item with id {id} not found in inventory.")

def update_item(id, name=None, price=None, availability=None, quantity=None):
    if id in inventory:
        item = inventory[id]
        if name is not None:
            item["name"] = name
        if price is not None:
            item["price"] = price
        if availability is not None:
            item["availability"] = availability
        if quantity is not None:
            item["quantity"] = quantity
        print(f"Item with id {id} has been updated")
    else:
        print(f"Item with id {id} not found")

def record_sale(id, quantity_sold):
    if id in inventory:
        item = inventory[id]
        if item["availability"] and item["quantity"] >= quantity_sold:
            item["quantity"] -= quantity_sold
            sale_amount = quantity_sold * item["price"]
            sales.append({"id": id, "quantity_sold": quantity_sold, "sale_amount": sale_amount})
            print(f"Sale recorded for Item ID {id}")
        elif not item["availability"]:
            print(f"{item['name']} is not available for sale.")
        else:
            print(f"Insufficient stock of {item['name']} for the sale.")
    else:
        print(f"Item with ID {id} not found in the inventory.")

def sales_report():
    total_sales = len(sales)
    total_amount_received = sum(sale["sale_amount"] for sale in sales)

    print(f"Total sales transactions: {total_sales}")
    print(f"Total amount received: ${total_amount_received:.2f}")

    print("Sales Report")
    for sale in sales:
        id = sale["id"]
        quantity_sold = sale["quantity_sold"]
        sale_amount = sale["sale_amount"]
        item = inventory[id]
        print(f"ID: {id}, Name: {item['name']}, Quantity Sold: {quantity_sold}, Sale Amount: ${sale_amount:.2f}")

def inventory_report():
    print("Inventory Report:")
    for id, item in inventory.items():
        print(f"ID: {id}, Name: {item['name']}, Price: ${item['price']:.2f}, Availability: {item['availability']}, Quantity: {item['quantity']}")

def main():
    while True:
        print("\nOptions:")
        print("1. Add item to inventory")
        print("2. Update item details")
        print("3. Remove item from inventory")
        print("4. Record a sale")
        print("5. Generate inventory report")
        print("6. Generate sales report")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            id = input("Enter the item ID: ")  # Allow non-integer IDs
            name = input("Enter the item name: ")
            price = float(input("Enter the item price: "))
            availability = input("Is the item available for sale? (True/False): ").lower() == "true"
            quantity_input = input("Enter the quantity (press Enter to skip): ")
            quantity = int(quantity_input) if quantity_input.strip() else None
            add_item(id, name, price, availability, quantity)
        elif choice == '2':
            id = input("Enter the item ID to update: ")  # Allow non-integer IDs
            name = input("Enter the new name (press Enter to skip): ")
            price_input = input("Enter the new price (press Enter to skip): ")
            price = float(price_input) if price_input.strip() else None
            quantity_input = input("Enter the new quantity (press Enter to skip): ")
            quantity = int(quantity_input) if quantity_input.strip() else None
            availability_input = input("Is the item available for sale? (True/False, press Enter to skip): ")
            availability = availability_input.lower() == "true" if availability_input.strip() else None
            update_item(id, name, price, availability, quantity)
        elif choice == '3':
            id = input("Enter the item ID to remove: ")  # Allow non-integer IDs
            remove_item(id)
        elif choice == '4':
            id = input("Enter the item ID for the sale: ")  # Allow non-integer IDs
            quantity_sold = int(input("Enter the quantity sold: "))
            record_sale(id, quantity_sold)
        elif choice == '5':
            inventory_report()
        elif choice == '6':
            sales_report()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
