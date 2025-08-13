product_list = []

def add_product(product_list):
    name = input("Enter product name: ")
    qty_text = input("Enter product quantity: ")
    try:
        quantity = int(qty_text)
    except ValueError:
        print("Quantity must be an integer. Try again.")
        return
    product = {"name": name, "quantity": quantity}
    product_list.append(product)
    print(f"Added: {name} ({quantity})")

def show_products(product_list):
    print("Product List:")
    if not product_list:
        print("(empty)")
        return
    for i, product in enumerate(product_list, start=1):
        print(f"{i}. {product['name']} - {product['quantity']} units")

if __name__ == "__main__":
    pass
