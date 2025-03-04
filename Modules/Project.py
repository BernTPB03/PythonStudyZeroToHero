import os

products = []


def display_header():
    print("=====================================")
    print("     Simple Shopping List           ")
    print("=====================================")


def add_product():
    print("\nAdding a new product:")
    name = input("Product name: ")
    unit = input("Unit of measurement (Kilogram, Gram, Liter, Milliliter, Unit, Meter, Centimeter): ").capitalize()
    while unit not in ['Kilogram', 'Gram', 'Liter', 'Milliliter', 'Unit', 'Meter', 'Centimeter']:
        print("Invalid unit! Please try again.")
        unit = input("Unit of measurement (Kilogram, Gram, Liter, Milliliter, Unit, Meter, Centimeter): ").capitalize()

    try:
        quantity = float(input("Quantity: "))
    except ValueError:
        print("Invalid input! Quantity must be a number.")
        return

    description = input("Product description: ")
    product_id = len(products) + 1
    product = {
        "id": product_id,
        "name": name,
        "unit": unit,
        "quantity": quantity,
        "description": description
    }
    products.append(product)
    print(f"\nProduct '{name}' added successfully!")


def remove_product():
    try:
        product_id = int(input("\nEnter the product ID to remove: "))
        removed_product = None
        for product in products:
            if product['id'] == product_id:
                removed_product = product
                products.remove(product)
                break
        if removed_product:
            print(f"\nProduct '{removed_product['name']}' removed successfully!")
        else:
            print("\nProduct not found with that ID.")
    except ValueError:
        print("\nInvalid ID! Please try again.")


def search_products():
    name_search = input("\nEnter the name or part of the product name: ").lower()
    results = [product for product in products if name_search in product['name'].lower()]
    if results:
        print(f"\n{len(results)} product(s) found:")
        for product in results:
            print(
                f"ID: {product['id']} - Name: {product['name']} - Quantity: {product['quantity']} {product['unit']} - Description: {product['description']}")
    else:
        print("\nNo products found.")


def list_products():
    if products:
        print("\nProducts in the shopping list:")
        for product in products:
            print(
                f"ID: {product['id']} - Name: {product['name']} - Quantity: {product['quantity']} {product['unit']} - Description: {product['description']}")
    else:
        print("\nNo products in the list.")


def menu():
    while True:
        display_header()
        list_products()
        print("\nChoose an option:")
        print("1. Add product")
        print("2. Remove product")
        print("3. Search products")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            remove_product()
        elif choice == "3":
            search_products()
        elif choice == "4":
            print("\nExiting the program... Goodbye!")
            break
        else:
            print("\nInvalid option! Please try again.")


menu()
