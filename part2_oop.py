class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Store:
    def __init__(self):
        # private attribute สำหรับเก็บออบเจกต์ Product
        self.__products = []

    def add_product(self, name, quantity):
        product = Product(name, quantity)
        self.__products.append(product)
        print(f"Added: {name} ({quantity})")

    def show_products(self):
        print("Product List:")
        if not self.__products:
            print("(empty)")
            return
        for i, product in enumerate(self.__products, start=1):
            print(f"{i}. {product.name} - {product.quantity} units")

if __name__ == "__main__":
    # ตัวอย่างการทดสอบ
    # my_store = Store()
    # my_store.add_product("Laptop", 15)
    # my_store.add_product("Mouse", 50)
    # my_store.show_products()
    pass
